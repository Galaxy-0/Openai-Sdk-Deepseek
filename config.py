import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# API配置
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_API_BASE = "https://api.deepseek.com/v1"

# 模型配置
MODEL_CONFIG = {
    "model_name": "deepseek-chat",
    "temperature": 0.7,
    "max_tokens": 2000,
    "top_p": 0.95,
    "frequency_penalty": 0.0,
    "presence_penalty": 0.0
}

# 智能体配置
AGENT_CONFIGS = {
    "product_agent": {
        "name": "产品专家",
        "instructions": "你是一个产品信息专家，可以帮助用户查询产品信息。请用简洁专业的语言回答。",
        "temperature": 0.7
    },
    "math_agent": {
        "name": "数学专家",
        "instructions": "你是一个数学计算专家，可以帮助用户进行数学计算。请提供详细的计算过程。",
        "temperature": 0.3
    },
    "router": {
        "name": "问题路由器",
        "instructions": """
        你负责将用户的问题路由到合适的专家：
        - 如果是关于产品的问题，交给产品专家
        - 如果是关于计算的问题，交给数学专家
        - 对于其他问题，直接回答或询问更多信息
        """,
        "temperature": 0.5
    }
} 