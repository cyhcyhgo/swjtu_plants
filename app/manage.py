import os
from flask_script import Manager
from flask_migrate import MigrateCommand
from app import create_app

# 读取配置
config_name = os.environ.get('FLASK_CONFIG') or 'default'
# 创建Flask实例
app = create_app(config_name)
# 创建命令启动控制对象
manager = Manager(app)
# 添加数据库迁移命令
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    app.run()