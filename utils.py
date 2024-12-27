def success_response(data=None, message="success"):
    """
    成功响应格式
    """
    return {
        "code": 0,
        "data": data or {},
        "message": message
    }

def error_response(message="error", code=1):
    """
    错误响应格式
    """
    return {
        "code": code,
        "data": {},
        "message": message
    } 