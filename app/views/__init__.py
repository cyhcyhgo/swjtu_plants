# 蓝本配置
from .main import main
from .user import user
from .manager import manager

DEFAULT_BLUEPRINT = (
    (main, ''),
    (user, '/user'),
    (manager, '/manager'),
)


# 注册蓝本
def config_blueprint(app):
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)
