from sqlalchemy import Table

from App.extensions import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from flask import current_app, jsonify, render_template
from App.models.plant import Plants

# 联系表
Favorites = Table("favorites", db.metadata,
                  db.Column("id", db.Integer, primary_key=True),
                  db.Column('user_id', db.Integer, db.ForeignKey("users.id")),
                  db.Column('plant_id', db.Integer, db.ForeignKey("plants.id")))


class Users(UserMixin, db.Model):
    """用户数据表"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    username = db.Column(db.String(20), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    isAdministrator = db.Column(db.Integer, nullable=False)
    confirmed = db.Column(db.Boolean, default=True)
    favorites = db.relationship('Plants', backref='users', lazy='dynamic', secondary='favorites')

    @property
    def password(self):
        """密码字段的保护"""
        raise AttributeError('密码是不可读属性')

    @password.setter
    def password(self, password) -> None:
        """设置密码，加密存储"""
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password) -> bool:
        """校验密码"""
        return check_password_hash(self.password_hash, password)

    def generate_activate_token(self, expires_in=3600):
        """生成激活账户的token"""
        # 创建用于生成token的类，需要传递密钥和有效期
        s = Serializer(current_app.config["SECRET_KEY"], expires_in)
        # 生成包含有效信息（必须是字典数据）的token字符串
        return s.dumps({'id': self.id})

    @staticmethod
    def check_activate_token(token):
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            data = s.load(token)
        except BadSignature:
            return jsonify({'status': True, 'message': '无效的token！', 'isJump': False})
        except SignatureExpired:
            return jsonify({'status': True, 'message': 'token已失效！', 'isJump': False})
        user = Users.query.get(data.get('id'))
        if not user:
            return jsonify({'status': True, 'message': '激活的账户不存在！', 'isJump': False})
        # 若没有激活账户，则执行激活任务
        if not user.confirmed:
            user.confirmed = True
            db.session.add(user)
        return jsonify({'status': True, 'message': '激活成功！', 'isJump': True})

    def is_favorite(self, pid) -> bool:
        """判断是否收藏指定植物"""
        # 获取该用户所有收藏的植物列表
        favorites = self.favorites.all()
        for plants in favorites:
            if int(plants.id) == int(pid):
                return True
        return False

    def add_favorite(self, pid) -> None:
        """收藏指定植物"""
        p = Plants.query.get(pid)
        self.favorites.append(p)

    def del_favorite(self, pid) -> None:
        """取消收藏指定植物"""
        p = Plants.query.get(pid)
        self.favorites.remove(p)

    def __repr__(self):
        return '<User %s>' % self.username

    def __init__(self, username, password, isAdministrator=0, confirmed=True):
        self.username = username
        self.password = password
        self.isAdministrator = isAdministrator
        self.confirmed = confirmed


# 登录认证的回调
@login_manager.user_loader
def load_user(uid):
    """登录认证的回调"""
    return Users.query.get(int(uid))


@login_manager.unauthorized_handler
def unauthorized():
    """未登录时显示提示信息"""
    login_manager.login_message = '您需要登录后才能使用此功能！'
    return render_template('user/unauthorized.html', login_manager=login_manager)
