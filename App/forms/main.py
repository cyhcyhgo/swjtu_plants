from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class Search(FlaskForm):
    key = StringField('', render_kw={"id": "shuru", "type": "search"})
    submit1 = SubmitField('', render_kw={"id": "but", "value": "搜索"})


class Fenlei(FlaskForm):
    key = StringField('', render_kw={"id": "mystery_m"})
    submit2 = SubmitField('', render_kw={"id": "mystery_b"})


class Style(object):
    button_image = ''
    input_color = ''
    button_color = ''
    button_border = ''
    web_image = ''
    td_color = ''
    td_border = ''

    def __init__(self, tup):
        self.button_image = tup[0]
        self.input_color = tup[1]
        self.button_color = tup[2]
        self.button_border = tup[3]
        self.web_image = tup[4]
        self.td_color = tup[5]
        self.td_border = tup[6]
