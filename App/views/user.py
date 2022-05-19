from App.views import verificationCode
from flask import render_template, session, Blueprint

from App.forms import User_info, Register
from App.models import Users
from App.extensions import db

import os

basedir = os.path.abspath(os.path.dirname(__file__))

user = Blueprint('user', __name__)


# 验证码
@user.route('/imgCode')
def imgCode():
    return verificationCode.imageCode().getImgCode()


@user.route('/login', methods=['GET', 'POST'])
def login():
    form = User_info()
    message = ''
    is_alert = 0
    is_jump = 0
    is_administrator = 0
    if form.validate_on_submit():
        username = form.data['name']
        current_user = Users.query.filter(Users.username == username).first()
        is_administrator = int(form.data['isAdministrator'])
        if current_user:
            if current_user.verify_password(form.data['password']):
                if current_user.isAdministrator == 0 and is_administrator:
                    message = '您不是管理员'
                    is_alert = 1
                else:
                    message = '欢迎回来，' + current_user.username
                    session['user_name'] = current_user.username
                    session['user_id'] = current_user.id
                    session.permanent = True  # 默认为 31 天
                    is_alert = 1
                    is_jump = 1
            else:
                is_alert = 1
                message = '密码错误'
        else:
            is_alert = 1
            message = '用户名不存在'
    return render_template('user/login.html',
                           message=message,
                           form=form,
                           isJump=is_jump,
                           isAlert=is_alert,
                           isAdministrator=is_administrator)


@user.route('/reg', methods=['GET', 'POST'])
def reg():
    form = Register()
    message = ' '
    is_alert = 0
    is_jump = 0
    if form.validate_on_submit():
        username = form.data['username']
        password = form.data['password']
        password2 = form.data['password2']
        captcha = form.data['captcha'].lower()
        current_user = Users.query.filter(Users.username == username).first()
        if captcha != session['imageCode'].lower():
            is_alert = 1
            message = '验证码错误'
        elif current_user:
            is_alert = 1
            message = '该用户已经存在'
        elif password != password2:
            is_alert = 1
            message = '两次密码输入不一致'
        elif len(password) < 6:
            is_alert = 1
            message = '密码长度至少6个字符'
        else:
            new_user = Users(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            is_alert = 1
            message = '注册成功！即将跳转至登录界面'
            is_jump = 1
    return render_template('user/reg.html', message=message, form=form, isJump=is_jump, isAlert=is_alert)


@user.route('/contribute', methods=('GET', 'POST'))
def contribute():  # put application's code here

    return render_template(
        'user/contribute.html'
    )

