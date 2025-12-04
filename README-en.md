<div align="center">
    <h1>acli_doc</h1>
    <h2>aCLI Troubleshooting Service Command Description Document, one-stop troubleshooting and resolution of typical HCI faults</h2>
</div>

<br>
<div align="center">
<a href="README.md" target="_blank">简体中文</a> | English
</div>
<br>

<div align="center">
<a href="http://acli.sangfor.com.cn:6888/" target="_blank"><img src="./static/img/quickstart-en.png" alt="quick start"></a>
</div>

---

> This documentation is built using [Docusaurus](https://docusaurus.io/) for the aCLI command-line troubleshooting
> service  
> Copyright © 2025 Sangfor aCloud   
> This project is licensed under the **GNU General Public License v3.0**

---

## 1. Overview

This repository centrally manages all the command description documents and official usage examples of the `acli`
command system, providing:

- Command line user manual
- Typical troubleshooting cases
- ...

## 2. Get involved quickly

### 2.1 Preconditions

- Node.js ≥ 18
- Familiar with Markdown syntax (for document writing)

### 2.2 Document Modification Process

1. Locate the document to be modified
2. Modify and save locally

### 2.3 Local Deployment and Testing

After making the modifications and saving them, you can try to deploy or test them locally. The operation process is as
follows:

```bash
npm install           # Install project dependencies

# This Test
npm run start         # Starts the local development server with hot reload functionality
# Visit http://localhost:3000 to see live results

# Local Deployment
npm run generate    # Generate the latest command list document
npm run build       # Build the static website of the production version
npm run serve       # Start the server locally to preview the built website
```

> If deployed in a container, add NODE_OPTIONS='--localstorage-file=/tmp/localstorage' before all npm actions.

## 3. Online access

Currently, the only official website [acli_doc](http://acli.sangfor.com.cn:6888/) (such as unable to open, please check
the DNS/agent, or try again later, the server may be temporarily inaccessible network fluctuations.)

## 4. Open Source Statement

- The document framework is based on [Docusaurus](https://docusaurus.io/) (MIT License). Special, thanks!
- This project as a whole is licensed under GPL-3.0. Any secondary distribution or derivative works must comply with the
  terms of the LICENSE.

## 5. Code of Conduct

Please abide by [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) and jointly maintain a friendly community.

## 6. Update the log

For details, see [CHANGELOG.md](./CHANGELOG.md).
