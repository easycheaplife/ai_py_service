from flask import Flask, jsonify, request
from zhipu_service import analyze_image

# 创建 Flask 应用实例
app = Flask(__name__)

# 根路由
@app.route('/')
def home():
    return 'Welcome to Flask Server!'

# GET 请求示例
@app.route('/hello')
def hello():
    return 'Hello, World!'

# 返回 JSON 数据的路由
@app.route('/api/data')
def get_data():
    data = {
        'message': '这是一个示例 API',
        'status': 'success',
        'data': [1, 2, 3, 4, 5]
    }
    return jsonify(data)

# 智谱AI图像识别API
@app.route('/api/image-recognition', methods=['POST'])
def image_recognition():
    try:
        # 获取POST请求中的图片URL
        request_data = request.get_json()
        image_url = request_data.get('image_url')
        
        if not image_url:
            return jsonify({
                'status': 'error',
                'message': '未提供图片URL'
            }), 400

        # 调用智谱AI服务
        result = analyze_image(image_url)
        
        # 返回识别结果
        return jsonify({
            'status': 'success',
            'result': result
        })
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    # 启动服务器，开启调试模式
    app.run(debug=True) 