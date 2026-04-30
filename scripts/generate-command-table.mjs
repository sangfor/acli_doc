#!/usr/bin/env node
import { promises as fs } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, '..');
const DOCS_DIR = path.join(ROOT_DIR, 'docs');
const I18N_EN_DOCS_DIR = path.join(ROOT_DIR, 'i18n/en/docusaurus-plugin-content-docs/current');
const CSV_PATH = path.join(DOCS_DIR, 'commandList.csv');
const COMMAND_LIST_MD_PATH = path.join(DOCS_DIR, 'commandList.md');
const COMMAND_LIST_MD_EN_PATH = path.join(I18N_EN_DOCS_DIR, 'commandList.md');
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

        // 中文文档汇总（优先中文，始终从源文档提取）
        const content = await fs.readFile(file, 'utf8');
        const summaryZh = extractSummary(content);

        // 英文文档汇总（从英文翻译文档提取摘要，用于英文列表）
        let summaryEn = summaryZh;
        const enFile = path.join(I18N_EN_DOCS_DIR, path.relative(DOCS_DIR, file));
        let summary = summaryZh;
        try {
            const enContent = await fs.readFile(enFile, 'utf8');
            const s = extractSummary(enContent);
            if (s) {
                summary = s;
                summaryEn = s;
            }
        } catch (e) {
            // 英文文档不存在
        }

        if (!summary) {
            continue;
        }

        rows.push({
            command,
            summary,
            summaryZh,
            summaryEn,
            source: path.relative(ROOT_DIR, file)
        });
    }

    if (!rows.length) {
        throw new Error('未在 docs 目录中找到任何 acli 命令。');
    }

    rows.sort((a, b) => a.command.localeCompare(b.command, 'zh-Hans-CN'));

    await fs.writeFile(CSV_PATH, buildCsv(rows), 'utf8');
    await updateCommandListMarkdown(buildMarkdownTable(rows), COMMAND_LIST_MD_PATH, 'zh');
    await updateCommandListMarkdown(buildMarkdownTableEn(rows), COMMAND_LIST_MD_EN_PATH, 'en');

    console.log(`已收集 ${rows.length} 条命令，生成文件：`);
    console.log(`- CSV: ${path.relative(ROOT_DIR, CSV_PATH)}`);
    console.log(`- Markdown: ${path.relative(ROOT_DIR, COMMAND_LIST_MD_PATH)}`);
    console.log(`- EN Markdown: ${path.relative(ROOT_DIR, COMMAND_LIST_MD_EN_PATH)}`);
}

async function collectMarkdownFiles(dir) {
    const entries = await fs.readdir(dir, { withFileTypes: true });
    const files = [];

    for (const entry of entries) {
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
    // 去除行尾空格，避免"空行"实际上是空格的情况（如 docs/plugin/info.md）
    const normalized = content.replace(/[ \t]+$/gm, '');
    const singleLineRegexes = [
        /### 操作概述\s*\n+([^\n]+)/,
        /### 命令概述\s*\n+([^\n]+)/,
        /### 命令描述\s*\n+([^\n]+)/,
        /### Overview\s*\n+([^\n]+)/,
        /### Command Overview\s*\n+([^\n]+)/,
        /### Description\s*\n+([^\n]+)/,
    ];
    for (const regex of singleLineRegexes) {
        const match = normalized.match(regex);
        if (match) return match[1].trim();
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

// 中文 Markdown 表格（使用中文摘要）
function buildMarkdownTable(rows) {
    const header = '| acli命令 | 命令操作概述 |';
    const divider = '| :---: | :---: |';
    const body = rows.map(({ command, summaryZh }) => {
        return `| ${markdownEscape(command)} | ${markdownEscape(summaryZh)} |`;
    });

    return [header, divider, ...body].join('\n');
}

// 英文 Markdown 表格（使用英文摘要）
function buildMarkdownTableEn(rows) {
    const header = '| acli Command | Command Overview |';
    const divider = '| :---: | :---: |';
    const body = rows.map(({ command, summaryEn }) => {
        return `| ${markdownEscape(command)} | ${markdownEscape(summaryEn)} |`;
    });

    return [header, divider, ...body].join('\n');
}

function markdownEscape(value) {
    return value.replace(/\|/g, '\\|');
}

async function updateCommandListMarkdown(tableContent, filePath, locale) {
    const now = new Date().toISOString().slice(0, 10);

    const templates = {
        zh: [
            `**\`更新时间: ${now}\`**`,
            ':::info 以下是最新的命令列表',
            ':::',
            '',
            tableContent,
            ''
        ],
        en: [
            `**\`Updated: ${now}\`**`,
            ':::info Below is the latest command list',
            ':::',
            '',
            tableContent,
            ''
        ]
    };

    const template = templates[locale].join('\n');

    let frontMatter = '';
    // 英文版本使用独立的 frontmatter
    if (locale === 'en') {
        frontMatter = [
            '---',
            'sidebar_position: 2',
            'sidebar_label: Command List',
            'title: aCLI Command List',
            '---',
            ''
        ].join('\n') + '\n';
    } else {
        try {
            const current = await fs.readFile(filePath, 'utf8');
            const fmMatch = current.match(/^---[\s\S]*?---/);
            if (fmMatch) {
                frontMatter = fmMatch[0].trim() + '\n\n';
            }
        } catch (error) {
            if (error.code !== 'ENOENT') {
                throw error;
            }
        }
    }

    const nextContent = `${frontMatter}${template}`.trimEnd() + '\n';
    await fs.writeFile(filePath, nextContent, 'utf8');
}

main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});