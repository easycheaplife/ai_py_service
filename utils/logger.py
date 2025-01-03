import logging
import time
from functools import wraps
from flask import request, g
import json
from logging.handlers import TimedRotatingFileHandler
import os
from datetime import datetime

# 创建日志目录
log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# 获取当前日期
current_date = datetime.now().strftime('%Y-%m-%d')

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# 创建 TimedRotatingFileHandler
file_handler = TimedRotatingFileHandler(
    filename=os.path.join(log_dir, f'app.{current_date}.log'),  # 包含日期的文件名
    when='midnight',  # 每天午夜切割
    interval=1,       # 每1天切割一次
    backupCount=30,   # 保留30天的日志
    encoding='utf-8'
)

# 设置日志格式
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# 自定义文件名后缀
def namer(default_name):
    """自定义日志文件名"""
    # 从默认文件名中提取日期
    date = default_name.split('.')[-2]
    return f"app.{date}.log"

file_handler.namer = namer

# 添加处理器
logger.addHandler(file_handler)

def log_request():
    """记录请求信息"""
    g.start_time = time.time()
    
    # 获取请求数据
    request_data = None
    if request.is_json:
        request_data = request.get_json()
    elif request.form:
        request_data = dict(request.form)
    elif request.args:
        request_data = dict(request.args)
        
    # 记录请求信息
    logger.info(
        f"Request: {request.method} {request.path}\n"
        f"Headers: {dict(request.headers)}\n"
        f"Data: {request_data}"
    )

def log_response(response):
    """记录响应信息"""
    # 计算请求处理时间
    duration = time.time() - g.start_time
    
    # 尝试解析响应数据
    try:
        response_data = json.loads(response.get_data())
    except:
        response_data = str(response.get_data())
    
    # 记录响应信息
    logger.info(
        f"Response: {response.status_code}\n"
        f"Duration: {duration:.2f}s\n"
        f"Data: {response_data}"
    )
    
    return response 