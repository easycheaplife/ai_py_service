from flask import Flask, jsonify, request, Response, stream_with_context
from zhipu_service import analyze_image, chat_with_ai
from utils import success_response, error_response

# 创建 Flask 应用实例
app = Flask(__name__)

# 根路由
@app.route('/')
def home():
    return jsonify(success_response(message="Welcome to Flask Server!"))

# GET 请求示例
@app.route('/hello')
def hello():
    return jsonify(success_response(message="Hello, World!"))

# 返回 JSON 数据的路由
@app.route('/api/data')
def get_data():
    data = {
        'items': [1, 2, 3, 4, 5]
    }
    return jsonify(success_response(data=data))

# 智谱AI图像识别API
@app.route('/api/image-recognition', methods=['POST'])
def image_recognition():
    try:
        # 获取POST请求中的图片URL和问题
        request_data = request.get_json()
        image_url = request_data.get('image_url')
        question = request_data.get('question', '图里有什么')  # 如果没有提供问题，使用默认值
        
        if not image_url:
            return jsonify(error_response(message="未提供图片URL")), 400

        # 调用智谱AI服务
        result = analyze_image(image_url, question)
        
        # 返回识别结果
        return jsonify(success_response(data=result))
        
    except Exception as e:
        return jsonify(error_response(message=str(e))), 500 

# 智谱AI聊天API
@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        # 获取请求数据
        request_data = request.get_json()
        messages = request_data.get('messages')
        
        if not messages:
            return jsonify(error_response(message="未提供对话内容")), 400

        # 调用智谱AI服务
        result = chat_with_ai(messages)
        
        # 返回结果
        return jsonify(success_response(data=result))
        
    except Exception as e:
        return jsonify(error_response(message=str(e))), 500 