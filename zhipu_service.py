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

def chat_with_ai(messages):
    """
    与智谱AI进行对话
    """
    client = ZhipuAI(api_key=config.ZHIPUAI_API_KEY)
    
    # 添加系统提示
    if not any(msg.get('role') == 'system' for msg in messages):
        messages.insert(0, {
            "role": "system",
            "content": "你是一个乐于回答各种问题的小助手，你的任务是提供专业、准确、有洞察力的建议。"
        })
    
    response = client.chat.completions.create(
        model="glm-4-flash",
        messages=messages,
        stream=False  # 关闭流式输出
    )
    
    # 将响应转换为可序列化的字典
    message = response.choices[0].message
    return {
        'role': message.role,
        'content': message.content
    } 