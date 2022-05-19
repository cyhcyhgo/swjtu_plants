from flask import Flask
from .views import config_blueprint
from .extensions import config_extensions
from .config import Config


def create_app(configName = "default"):
    """初始化app实例"""
    app = Flask(__name__)
    # 加载配置文件内容
    config_dic = Config()
    app.config.from_object(config_dic)
    # 注册蓝本
    config_blueprint(app)
    # 初始化扩展库
    config_extensions(app)
    return app
