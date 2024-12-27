# 环境配置
class Config:
    # 基础配置
    DEBUG = False
    HOST = '0.0.0.0'
    PORT = 5000

class DevelopmentConfig(Config):
    # 开发环境
    DEBUG = True

class ProductionConfig(Config):
    # 生产环境
    DEBUG = False

# 配置映射
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
} 