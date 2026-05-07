import { themes as prismThemes } from "prism-react-renderer";
import type { Config } from "@docusaurus/types";
import type * as Preset from "@docusaurus/preset-classic";

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: "aCLI",
  tagline: "深信服HCI命令行工具",
  favicon: "img/favicon.ico",

  // Set the production url of your site here
  url: "http://acli.sangfor.com.cn:6888/",
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: "/",

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  //organizationName: 'facebook', // Usually your GitHub org/user name.
  //projectName: 'docusaurus', // Usually your repo name.

  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: "zh-Hans",
    locales: ["zh-Hans", "en"],
  },

  presets: [
    [
      "@docusaurus/preset-classic",
      {
        docs: {
          path: 'docs',
          routeBasePath: '/',
          sidebarPath: "./sidebars.ts",
          editUrl:
            "https://github.com/sangfor/acli_doc/blob/main",
          // 启用版本控制，包括当前版本
          lastVersion: "current",
          versions: {
            current: {
              label: "开发中 🚧",
              path: "/"
            },
            // "1.0.1": { label: "1.0.1" },
          },
        },
        blog: false,
        theme: {
          customCss: "./src/css/custom.css",
        },
      } satisfies Preset.Options,
    ],
  ],

  plugins: [
    [
      require.resolve("@easyops-cn/docusaurus-search-local"),
      ({
        hashed: true, // 生成带哈希的文件名
        language: ["zh", "en"], // 支持的语言
        indexDocs: true, // 是否索引文档
        indexPages: true, // 是否索引独立页面
        indexBlog: false, // 是否索引博客
        docsRouteBasePath: "/", // 文档的路由基础路径
        highlightSearchTermsOnTargetPage: true, // 在目标页面高亮搜索词
        explicitSearchResultPath: true, // 显示明确的搜索结果路径
      }),
    ],
  ],

  themeConfig: {
    // themeConfig.image 主要用于设置社交卡片的图片，需要被其他网站抓取展示时则需要设置
    // image: 'img/social-card.jpg',
    navbar: {
      title: "aCLI",
      logo: {
        alt: "aCLI Logo",
        src: "img/logo.svg",
      },
      items: [
        {
          type: "docSidebar",
          sidebarId: "tutorialSidebar",
          position: "left",
          label: "命令说明文档",
        },
        {
          type: 'docsVersionDropdown',
          position: "right",
        },
        {
          type: "localeDropdown",
          position: "right",
        },
        {
          href: "https://support.sangfor.com.cn/",
          label: "深信服技术支持",
          position: "right",
        },
      ],
    },
    footer: {
      style: "dark",
      copyright: `Copyright © ${new Date().getFullYear()} Sangfor, Inc. Built with LMT.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
