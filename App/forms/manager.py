from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class Manage_user_info(FlaskForm):
    user_id = StringField('', validators=[DataRequired()], render_kw={"type": "text", })
    name = StringField('', validators=[DataRequired()],
                       render_kw={"id": "user_name", "type": "text", "placeholder": "用户名", 'maxlength': '20'})
    password = PasswordField('', validators=[DataRequired()],
                             render_kw={"id": "password", "placeholder": "密码", 'maxlength': '10', 'minlength': '6'})
    isAdministrator = BooleanField('', render_kw={"id": "check"})
    submit = SubmitField('登录', render_kw={"class": "btn btn-primary"})