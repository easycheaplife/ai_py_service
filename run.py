import os
from app import app
from settings import config

# 默认使用开发环境
env = os.getenv('FLASK_ENV', 'development')
config_obj = config[env]

def main():
    # 应用配置
    app.config.from_object(config_obj)
    
    # 输出启动信息
    print(f"Starting server in {env} mode")
    print(f"Server running on http://{app.config['HOST']}:{app.config['PORT']}")
    print(f"Debug mode: {app.config['DEBUG']}")
    
    # 启动服务器
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )

if __name__ == '__main__':
    main() 