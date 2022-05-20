from flask import render_template, request, session, jsonify, Blueprint

from App.extensions import db
from App.forms import Manage_user_info
from App.models import Plants, Info, Position, Picture, Users

manager = Blueprint('manager', __name__)


@manager.route('/plants_manage', methods=('GET', 'POST'))
def plants_manage():  # put application's code here
    """植物管理页面"""
    xianshi_t = []
    for plant in Plants.query.all():
        id_p = plant.id
        position = Position.query.filter_by(id=id_p).first()
        info = Info.query.filter_by(id=id_p).first()
        picture = Picture.query.filter_by(id=id_p).first()
        dic = {'id': id_p,
               'name': plant.plant_name,
               'time': plant.time,
               'language': plant.language,
               'longitude': position.longitude,
               'latitude': position.latitude,
               'area': position.area[0:3],
               'academic': info.academic,
               'literary': info.literary}
        xianshi_t.append(dic)
    return render_template(
        'manager/plant_manage.html', xianshi=xianshi_t
    )


@manager.route('/user_manage', methods=('GET', 'POST'))
def user_manage():
    """用户信息管理"""
    form = Manage_user_info()
    xianshi_t = []
    count = 1
    for user in Users.query.all():
        id_u = user.id
        dic = {'id': id_u,
               'username': user.username,
               'password': user.password_hash[0:40]+'...',
               'isAdministrator': '是' if user.isAdministrator == 1 else '否',
               'count': count}
        xianshi_t.append(dic)
        count = count + 1
    return render_template(
        'manager/user_manage.html', xianshi=xianshi_t, form=form
    )


@manager.route('/edit', methods=('GET', 'POST'))
def edit():
    """修改用户信息"""
    user_id = request.args.get('user_id')
    user_name = request.args.get('name')
    password = request.args.get('password')
    is_administrator = request.args.get('isAdministrator')
    current_user = Users.query.filter(Users.username.ilike(user_name)).first()
    if is_administrator is None and str(session['user_id']) == str(user_id):
        return jsonify({'status': True, 'message': '不能撤销自己的管理员权限', 'isJump': False})
    elif current_user and str(user_id) != str(current_user.id):
        # 用户名不区分大小写
        return jsonify({'status': True, 'message': '该用户名已存在', 'isJump': False})
    else:
        current_user = Users.query.filter(Users.id == str(user_id)).first()
        current_user.username = user_name
        current_user.password = password
        current_user.isAdministrator = 0 if (is_administrator is None) else 1
        db.session.add(current_user)
        db.session.commit()
        return jsonify({'status': True, 'message': '修改成功！', 'isJump': True})


@manager.route('/delete', methods=('GET', 'POST'))
def delete():
    """删除用户"""
    user_id = request.args.get('user_id')
    delete_user = Users.query.filter(Users.id == str(user_id)).first()
    if str(session['user_id']) == str(user_id):
        return jsonify({'status': True, 'message': '不能删除自己的账户', 'isJump': False})
    else:
        db.session.delete(delete_user)
        db.session.commit()
        return jsonify({'status': True, 'message': '删除成功！', 'isJump': True})
