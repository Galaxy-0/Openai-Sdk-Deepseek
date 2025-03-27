import asyncio
from agents import Agent, Runner, trace
from deepseek_config import DeepSeekModelConfig
from tools import search_database, calculate, get_product_recommendations
from config import AGENT_CONFIGS, MODEL_CONFIG

async def create_agents():
    """创建所有智能体"""
    # 创建模型配置
    model_config = DeepSeekModelConfig(**MODEL_CONFIG)
    
    # 创建产品专家智能体
    product_agent = Agent(
        name=AGENT_CONFIGS["product_agent"]["name"],
        instructions=AGENT_CONFIGS["product_agent"]["instructions"],
        tools=[search_database, get_product_recommendations],
        model_config=model_config
    )
    
    # 创建数学专家智能体
    math_agent = Agent(
        name=AGENT_CONFIGS["math_agent"]["name"],
        instructions=AGENT_CONFIGS["math_agent"]["instructions"],
        tools=[calculate],
        model_config=model_config
    )
    
    # 创建路由智能体
    router = Agent(
        name=AGENT_CONFIGS["router"]["name"],
        instructions=AGENT_CONFIGS["router"]["instructions"],
        handoffs=[product_agent, math_agent],
        model_config=model_config
    )
    
    return router

async def main():
    print("===== DeepSeek智能助手 =====")
    print("我可以帮您：")
    print("1. 查询产品信息")
    print("2. 进行数学计算")
    print("3. 推荐产品")
    print("输入'退出'结束对话\n")
    
    try:
        # 创建智能体
        router = await create_agents()
        
        while True:
            user_input = input("\n请输入您的问题: ")
            if user_input.lower() in ["退出", "exit", "quit"]:
                print("\n感谢使用，再见！")
                break
            
            try:
                with trace("用户对话"):
                    result = await Runner.run(router, user_input)
                    print(f"\n回答: {result.final_output}")
            except Exception as e:
                print(f"\n抱歉，处理您的请求时出现错误: {str(e)}")
                
    except Exception as e:
        print(f"\n系统错误: {str(e)}")
        print("请检查API密钥配置是否正确")

if __name__ == "__main__":
    asyncio.run(main()) 