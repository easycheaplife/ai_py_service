
# ai_py_service

基于 Python 的 AI 服务，集成了 ZhipuAI 图像识别与对话能力，提供 RESTful API 接口。

## 主要功能

- 图像识别：调用 ZhipuAI 接口分析图片内容
- 智能对话：与 ZhipuAI 进行多轮对话
- 基础 API 示例：如 `/hello`、`/api/data` 等

## 安装依赖

```bash
pip install flask zhipuai
```

## 运行服务

```bash
python run.py
```

默认运行在 `0.0.0.0:5000`，可通过环境变量 `FLASK_ENV` 切换开发/生产模式。

## API 说明

- `GET /`  
	返回欢迎信息

- `GET /hello`  
	返回 Hello World 示例

- `POST /api/image-recognition`  
	请求体：`{"image_url": "图片URL"}`  
	返回：图片识别结果

- `POST /api/chat`  
	请求体：`{"messages": [...]}`  
	返回：AI 对话结果

## 配置

- API Key 配置在 `config.py` 文件中
- 其他服务参数见 `settings.py`

## 目录结构

- `app.py`：Flask 路由与主逻辑
- `run.py`：服务启动入口
- `config.py`：API Key 配置
- `settings.py`：环境参数
- `utils.py`：通用响应格式
- `zhipu_service.py`：ZhipuAI 接口封装

---
