from zhipuai import ZhipuAI
import config

def analyze_image(image_url):
    """
    调用智谱AI接口分析图片
    """
    client = ZhipuAI(api_key=config.ZHIPUAI_API_KEY)
    
    response = client.chat.completions.create(
        model="glm-4v-flash",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "图里有什么"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url
                        }
                    }
                ]
            }
        ]
    )
    
    # 将 CompletionMessage 对象转换为可序列化的字典
    message = response.choices[0].message
    return {
        'role': message.role,
        'content': message.content
    } 