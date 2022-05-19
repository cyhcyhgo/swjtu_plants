from flask_script import Manager
from flask_migrate import MigrateCommand
import sys
import os

sys.path.append(os.path.dirname(sys.path[0]))
from App.create import create_app

# 读取配置
config_name = os.environ.get('FLASK_CONFIG') or 'default'
# 创建Flask实例
app = create_app(config_name)
# 创建命令启动控制对象
manager = Manager(app)
# 添加数据库迁移命令
manager.add_command('db', MigrateCommand)


# 错误界面
@app.errorhandler(404)
def page_not_found(e):
    return '@_@ 出错了：404', 404


@app.errorhandler(500)
def page_not_found(e):
    return '@_@ 出错了：500', 500


if __name__ == '__main__':
    manager.run()
