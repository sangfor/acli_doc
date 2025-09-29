# 贡献指南 (CONTRIBUTING)

## 欢迎贡献

感谢您对 `acli_doc` 项目的关注！我们欢迎各种形式的贡献。  
`acli_doc`是我们希望帮助`acli`的使用者快速学习和方便查找的手册。  
同时`acli_doc`也是我们面向所有的开发者和使用者的一个沟通交流的通道。  

## 参与其中

### 1. 文档贡献

- 改进现有文档的准确性、完整性和可读性
- 添加新的使用示例和教程
- 翻译文档内容
- 修正拼写和语法错误

## 工作流程

### 1. 提交问题和需求

在开始任何开发工作之前，请先查看项目的 `issue` 列表。如果您发现新问题或有功能需求，请按以下步骤操作：

1. 访问项目的 issue 跟踪页面
2. 搜索是否已有相关 issue
3. 如果没有，创建新的 issue 并详细描述：
   - 问题的具体表现
   - 复现步骤（对于 bug）
   - 预期行为
   - 相关环境信息

### 2. 提交流程

```bash
# 1. Fork 项目到您的账户
# 2. 克隆您的 fork 到本地
git clone https://github.com/your-username/acli_doc.git

# 3. 添加上游仓库
git remote add upstream https://github.com/original-owner/acli_doc.git

# 4. 创建新分支进行开发
git checkout -b feature/your-feature-name

# 5. 进行修改和开发
# 6. 提交更改
git add .
git commit -m "描述您的更改"

# 7. 推送到您的 fork
git push origin feature/your-feature-name
```

### 3. 提交合并请求

1. 确保您的分支与上游主分支保持同步
2. 在 GitHub 上创建 Pull Request
   - 选择正确的源分支和目标分支
   - 提供清晰的标题和描述
   - 关联相关的 issue（如果有的话）
   - 等待代码审查和反馈

```bash
git fetch upstream
git checkout main
git merge upstream/main
git checkout feature/your-feature-name
git rebase main
```

## 提交规范

- 文档为markdown格式
- 符合acli的命令规范
- 编写清晰的提交信息

## 联系我们

除了在项目中提交issue跟我们保持对话外，我们还提供邮件方式；  
可发送邮件至[acli@sangfor.com.cn](mailto:acli@sangfor.com.cn)来寻求帮助。  

## 社区行为准则

请遵守项目的社区行为准则，尊重所有贡献者，营造友好、包容的开发环境。

再次感谢您的贡献！
