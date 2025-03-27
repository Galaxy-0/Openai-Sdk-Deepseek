# 贡献指南

感谢您对OpenAI Agents SDK with DeepSeek项目的关注！我们欢迎任何形式的贡献。

## 开发流程

1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

## 代码规范

- 使用 Black 进行代码格式化
- 使用 Pylint 进行代码检查
- 确保所有测试通过
- 保持代码覆盖率在80%以上

## 提交信息规范

提交信息应该遵循以下格式：
```
<type>(<scope>): <subject>

<body>

<footer>
```

类型（type）：
- feat: 新功能
- fix: 修复bug
- docs: 文档更新
- style: 代码格式（不影响代码运行的变动）
- refactor: 重构
- test: 增加测试
- chore: 构建过程或辅助工具的变动

## 环境设置

1. 克隆仓库：
```bash
git clone https://github.com/yourusername/Openai-Sdk-Deepseek.git
cd Openai-Sdk-Deepseek
```

2. 创建虚拟环境：
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

4. 复制环境变量模板：
```bash
cp .env.example .env
```

5. 编辑 `.env` 文件，填入您的API密钥

## 运行测试

```bash
pytest
```

## 代码格式化

```bash
black .
```

## 代码检查

```bash
pylint **/*.py
```

## 许可证

通过提交代码，您同意您的代码将使用与项目相同的许可证（MIT License）。 