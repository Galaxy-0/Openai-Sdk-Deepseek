# OpenAI Agents SDK with DeepSeek

这是一个使用OpenAI Agents SDK和DeepSeek API构建的智能助手示例项目。

## 功能特点

- 使用DeepSeek API作为底层模型
- 多智能体协作系统
- 产品信息查询
- 数学计算
- 产品推荐

## 项目结构

```
Openai-Sdk-Deepseek/
├── .env                    # 环境变量配置
├── config.py              # 配置文件
├── deepseek_config.py     # DeepSeek模型配置
├── main.py               # 主应用
├── requirements.txt      # 项目依赖
├── tools.py             # 工具函数
└── README.md            # 项目说明
```

## 安装步骤

1. 克隆项目：
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

4. 配置环境变量：
- 复制`.env.example`为`.env`
- 在`.env`文件中设置你的DeepSeek API密钥：
```
DEEPSEEK_API_KEY=your_deepseek_api_key_here
```

## 使用方法

运行主程序：
```bash
python main.py
```

## 示例对话

1. 查询产品信息：
```
请输入您的问题: 请告诉我产品A的信息
```

2. 数学计算：
```
请输入您的问题: 计算23乘以45等于多少
```

3. 产品推荐：
```
请输入您的问题: 预算200元，想要一个实用的产品
```

## 注意事项

- 确保已正确设置DeepSeek API密钥
- 检查网络连接是否正常
- 确保Python版本 >= 3.10

## 许可证

MIT License
