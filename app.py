from flask import Flask, jsonify, request
from zhipu_service import analyze_image
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
        # 获取POST请求中的图片URL
        request_data = request.get_json()
        image_url = request_data.get('image_url')
        
        if not image_url:
            return jsonify(error_response(message="未提供图片URL")), 400

        # 调用智谱AI服务
        result = analyze_image(image_url)
        
        # 返回识别结果
        return jsonify(success_response(data=result))
        
    except Exception as e:
        return jsonify(error_response(message=str(e))), 500 