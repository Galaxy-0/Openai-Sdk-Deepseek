from typing import Any, Dict, List, Optional
from agents import ModelConfig, ModelResponse
import httpx
from config import DEEPSEEK_API_KEY, DEEPSEEK_API_BASE

class DeepSeekModelConfig(ModelConfig):
    """DeepSeek模型配置"""
    
    def __init__(
        self,
        api_key: str = DEEPSEEK_API_KEY,
        model_name: str = "deepseek-chat",
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        **kwargs
    ):
        if not api_key:
            raise ValueError("DeepSeek API密钥不能为空")
            
        self.api_key = api_key
        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.kwargs = kwargs
        
    async def generate(
        self,
        messages: List[Dict[str, str]],
        **kwargs
    ) -> ModelResponse:
        """调用DeepSeek API生成响应"""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": self.model_name,
            "messages": messages,
            "temperature": self.temperature,
            **self.kwargs
        }
        
        if self.max_tokens:
            data["max_tokens"] = self.max_tokens
            
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{DEEPSEEK_API_BASE}/chat/completions",
                    headers=headers,
                    json=data,
                    timeout=30.0
                )
                
                if response.status_code != 200:
                    error_msg = f"API调用失败: {response.text}"
                    print(f"错误详情: {error_msg}")
                    raise Exception(error_msg)
                    
                result = response.json()
                
                return ModelResponse(
                    content=result["choices"][0]["message"]["content"],
                    model=self.model_name,
                    usage=result["usage"]
                )
                
        except httpx.TimeoutException:
            raise Exception("API请求超时")
        except httpx.RequestError as e:
            raise Exception(f"API请求错误: {str(e)}")
        except Exception as e:
            raise Exception(f"生成响应时发生错误: {str(e)}") 