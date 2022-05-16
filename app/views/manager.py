from flask import Flask, render_template, url_for, redirect, request, session, jsonify, Blueprint

from app.forms import Manage_user_info
from app.models import Plants, Info, Position, Picture, Users
from app.extensions import db
import os

manager = Blueprint('manager', __name__)


@manager.route('/plants_manage', methods=('GET', 'POST'))
def plants_manage():  # put application's code here
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
def user_manage():  # put application's code here
    form = Manage_user_info()
    xianshi_t = []
    count = 1
    for user in Users.query.all():
        id_u = user.id
        dic = {'id': id_u,
               'username': user.username,
               'password': user.password,
               'isAdministrator': '是' if user.isAdministrator == 1 else '否',
               'count': count}
        xianshi_t.append(dic)
        count = count + 1
    return render_template(
        'manager/user_manage.html', xianshi=xianshi_t, form=form
    )


@manager.route('/edit', methods=('GET', 'POST'))
def edit():  # 修改用户信息
    user_id = request.args.get('user_id')
    user_name = request.args.get('name')
    password = request.args.get('password')
    isAdministrator = request.args.get('isAdministrator')
    User = Users.query.filter(Users.username.ilike(user_name)).first()
    if isAdministrator is None and str(session['user_id']) == str(user_id):
        return jsonify({'status': True, 'message': '不能撤销自己的管理员权限', 'isJump': False})
    elif User and str(user_id) != str(User.id):
        # 用户名不区分大小写
        return jsonify({'status': True, 'message': '该用户名已存在', 'isJump': False})
    else:
        User = Users.query.filter(Users.id == str(user_id)).first()
        User.username = user_name
        User.password = password
        User.isAdministrator = 0 if (isAdministrator is None) else 1
        db.session.add(User)
        db.session.commit()
        return jsonify({'status': True, 'message': '修改成功！', 'isJump': True})


@manager.route('/delete', methods=('GET', 'POST'))
def delete():
    user_id = request.args.get('user_id')
    User = Users.query.filter(Users.id == str(user_id)).first()
    if str(session['user_id']) == str(user_id):
        return jsonify({'status': True, 'message': '不能删除自己的账户', 'isJump': False})
    else:
        db.session.delete(User)
        db.session.commit()
        return jsonify({'status': True, 'message': '删除成功！', 'isJump': True})
