#!/usr/bin/env node
import { promises as fs } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, '..');
const DOCS_DIR = path.join(ROOT_DIR, 'docs');
const CSV_PATH = path.join(DOCS_DIR, 'commandList.csv');
const COMMAND_LIST_MD_PATH = path.join(DOCS_DIR, 'commandList.md');
const MARKDOWN_EXTENSIONS = new Set(['.md', '.mdx']);

async function main() {
    const markdownFiles = await collectMarkdownFiles(DOCS_DIR);
    const rows = [];

    for (const file of markdownFiles) {
        if (path.resolve(file) === path.resolve(COMMAND_LIST_MD_PATH)) {
            continue;
        }

        const command = deriveCommandFromPath(file);
        if (!command) {
            continue;
        }

        const content = await fs.readFile(file, 'utf8');
        const summary = extractSummary(content);

        if (!summary) {
            continue;
        }

        rows.push({
            command,
            summary,
            source: path.relative(ROOT_DIR, file)
        });
    }

    if (!rows.length) {
        throw new Error('未在 docs 目录中找到任何 acli 命令。');
    }

    rows.sort((a, b) => a.command.localeCompare(b.command, 'zh-Hans-CN'));

    await fs.writeFile(CSV_PATH, buildCsv(rows), 'utf8');
    await updateCommandListMarkdown(buildMarkdownTable(rows));

    console.log(`已收集 ${rows.length} 条命令，生成文件：`);
    console.log(`- CSV: ${path.relative(ROOT_DIR, CSV_PATH)}`);
    console.log(`- Markdown: ${path.relative(ROOT_DIR, COMMAND_LIST_MD_PATH)}`);
}

async function collectMarkdownFiles(dir) {
    const entries = await fs.readdir(dir, { withFileTypes: true });
    const files = [];

    for (const entry of entries) {
        // 忽略隐藏目录与构建产物
        if (entry.name.startsWith('.')) {
            continue;
        }

        const entryPath = path.join(dir, entry.name);

        if (entry.isDirectory()) {
            files.push(...await collectMarkdownFiles(entryPath));
        } else if (MARKDOWN_EXTENSIONS.has(path.extname(entry.name).toLowerCase())) {
            files.push(entryPath);
        }
    }

    return files;
}

function extractSummary(content) {
    const summaryRegexes = [
        /操作概述[:：]\s*(.+)/,
        /命令概述[:：]\s*(.+)/,
        /命令描述[:：]\s*(.+)/
    ];

    for (const regex of summaryRegexes) {
        const match = content.match(regex);
        if (match) {
            return match[1].trim();
        }
    }

    return '';
}

function deriveCommandFromPath(file) {
    const relativePath = path.relative(DOCS_DIR, file);
    const segments = relativePath
        .split(path.sep)
        .map((segment, index, arr) => {
            if (index === arr.length - 1) {
                return segment.replace(/\.(md|mdx)$/i, '');
            }
            return segment;
        })
        .filter((segment) => segment && !isSkippedSegment(segment));

    if (segments.length < 2) {
        return '';
    }

    return `acli ${segments.join(' ')}`.trim();
}

function isSkippedSegment(segment) {
    const lowered = segment.toLowerCase();
    return lowered === 'index' || lowered === 'readme';
}

function buildCsv(rows) {
    const header = '命令,操作概述';
    const data = rows.map(({ command, summary }) => {
        return `${csvEscape(command)},${csvEscape(summary)}`;
    });

    return [header, ...data].join('\n') + '\n';
}

function csvEscape(value) {
    const safe = value.replace(/"/g, '""');
    return `"${safe}"`;
}

function buildMarkdownTable(rows) {
    const header = '| acli命令 | 命令操作概述 |';
    const divider = '| :---: | :---: |';
    const body = rows.map(({ command, summary }) => {
        return `| ${markdownEscape(command)} | ${markdownEscape(summary)} |`;
    });

    return [header, divider, ...body].join('\n');
}

function markdownEscape(value) {
    return value.replace(/\|/g, '\\|');
}

async function updateCommandListMarkdown(tableContent) {
    const now = new Date().toISOString().slice(0, 10);
    const template = [
        `**\`更新时间: ${now}\`**`,
        ':::info 以下是最新的命令列表',
        ':::',
        '',
        tableContent,
        ''
    ].join('\n');

    let frontMatter = '';
    try {
        const current = await fs.readFile(COMMAND_LIST_MD_PATH, 'utf8');
        const fmMatch = current.match(/^---[\s\S]*?---/);

        if (fmMatch) {
            frontMatter = fmMatch[0].trim() + '\n\n';
        }
    } catch (error) {
        if (error.code !== 'ENOENT') {
            throw error;
        }
    }

    const nextContent = `${frontMatter}${template}`.trimEnd() + '\n';
    await fs.writeFile(COMMAND_LIST_MD_PATH, nextContent, 'utf8');
}

main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
