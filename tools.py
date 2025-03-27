from agents import function_tool
from typing import Dict, List

@function_tool
def search_database(query: str) -> str:
    """搜索产品数据库获取信息"""
    # 模拟数据库
    database = {
        "产品A": {
            "价格": "100元",
            "库存": "200件",
            "描述": "高质量产品A，适合日常使用",
            "规格": "标准尺寸"
        },
        "产品B": {
            "价格": "200元",
            "库存": "150件",
            "描述": "高端产品B，适合专业用途",
            "规格": "大尺寸"
        },
        "产品C": {
            "价格": "300元",
            "库存": "100件",
            "描述": "定制产品C，支持个性化配置",
            "规格": "可定制"
        }
    }
    
    # 模糊匹配
    for product_name, info in database.items():
        if query.lower() in product_name.lower():
            return f"""
            产品名称: {product_name}
            价格: {info['价格']}
            库存: {info['库存']}
            描述: {info['描述']}
            规格: {info['规格']}
            """
    
    return f"未找到关于'{query}'的信息"

@function_tool
def calculate(expression: str) -> str:
    """计算数学表达式"""
    try:
        # 安全检查：只允许基本的数学运算
        allowed_chars = set("0123456789+-*/() .")
        if not all(c in allowed_chars for c in expression):
            return "错误：表达式包含不安全的字符"
            
        result = eval(expression)
        return f"表达式: {expression}\n计算结果: {result}"
    except Exception as e:
        return f"计算错误: {str(e)}"

@function_tool
def get_product_recommendations(budget: float, preferences: List[str]) -> str:
    """根据预算和偏好推荐产品"""
    # 模拟产品数据库
    products = [
        {"name": "产品A", "price": 100, "tags": ["日常", "实用", "经济"]},
        {"name": "产品B", "price": 200, "tags": ["专业", "高端", "耐用"]},
        {"name": "产品C", "price": 300, "tags": ["定制", "创新", "个性化"]}
    ]
    
    # 根据预算和偏好筛选产品
    recommendations = []
    for product in products:
        if product["price"] <= budget and any(pref in product["tags"] for pref in preferences):
            recommendations.append(product)
    
    if not recommendations:
        return f"抱歉，在预算{budget}元内没有找到符合您偏好的产品。"
    
    result = "推荐产品：\n"
    for product in recommendations:
        result += f"- {product['name']} (价格: {product['price']}元)\n"
        result += f"  特点: {', '.join(product['tags'])}\n"
    
    return result 