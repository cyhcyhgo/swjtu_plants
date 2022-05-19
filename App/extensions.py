from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate(db=db)
login_manager = LoginManager()


def config_extensions(app):
    """初始化扩展包"""
    db.init_app(app)
    migrate.init_app(app)
    # 登录认证
    login_manager.init_app(app)
    # 指定登录的端点
    login_manager.login_view = 'user.login'
    login_manager.login_message = '您需要登录后才能使用此功能！'
    login_manager.session_protection = 'strong'

