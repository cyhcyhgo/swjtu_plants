from flask import render_template, url_for, redirect, Blueprint
import os
import configparser
from App.forms import spring_style, summer_style, autumn_style, winter_style, Search, Fenlei, Style
from App.models import Plants, Info, Position, Picture, initial_database
from App.extensions import db

main = Blueprint('main', __name__)
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
cf = configparser.ConfigParser()
cf.read(basedir + r'\config.ini', encoding='utf-8')


@main.route('/', methods=('GET', 'POST'))
def index():  # 首页
    is_first_load = cf.getboolean("mysql", "is_first_load")
    if is_first_load:
        initial_database(db)
        cf.set("mysql", "is_first_load", "False")
        f = open(basedir + r'\config.ini', 'w')
        cf.write(f)
        f.close()
        del f
        print("!")
    form = Search()
    form2 = Fenlei()
    return render_template(
        'main/index.html', form=form, form2=form2
    )


@main.route('/search_2/<keyword>')
def search_2(keyword):  # 搜索界面
    form = Search()
    k = ''
    xianshi_t = []
    if keyword == 'any':
        for plant in Plants.query.all():
            id_p = plant.id
            position = Position.query.filter_by(id=id_p).first()
            info = Info.query.filter_by(id=id_p).first()
            picture = Picture.query.filter_by(id=id_p).first()
            dic = {'image': url_for('static', filename=picture.search_p),
                   'name': plant.plant_name,
                   'family': plant.family,
                   'area': position.area[0:3],
                   'brief': info.brief,
                   'href': url_for('main.season', id=id_p)}
            xianshi_t.append(dic)
        count = Plants.query.count()
    else:
        k = keyword
        for plant in Plants.query.filter(Plants.plant_name.ilike('%' + keyword + '%')).all():
            id_p = plant.id
            position = Position.query.filter_by(id=id_p).first()
            info = Info.query.filter_by(id=id_p).first()
            picture = Picture.query.filter_by(id=id_p).first()
            dic = {'image': url_for('static', filename=picture.search_p),
                   'name': plant.plant_name,
                   'family': plant.family,
                   'area': position.area[0:3],
                   'brief': info.brief,
                   'href': url_for('main.season', id=id_p)}
            xianshi_t.append(dic)
        count = Plants.query.filter(Plants.plant_name.ilike('%' + keyword + '%')).count()

    return render_template(
        'main/search_2.html',
        xianshi=xianshi_t,
        count=count,
        form=form,
        k=k
    )


@main.route('/fenlei/<keyword>')
def fenlei(keyword):
    form = Search()
    form2 = Fenlei()
    # k代表序号
    k = 1
    xianshi_t = []
    if keyword == '木本植物' or keyword == '草本植物':
        for plant in Plants.query.filter(Plants.type.ilike('%' + keyword + '%')).all():
            id_p = plant.id
            position = Position.query.filter_by(id=id_p).first()
            picture = Picture.query.filter_by(id=id_p).first()
            dic = {'image': url_for('static', filename=picture.search_p),
                   'type': plant.type,
                   'name': plant.plant_name,
                   'area': position.area,
                   'time': plant.time,
                   'href': url_for('main.season', id=id_p),
                   'k': k}
            xianshi_t.append(dic)
            k = k + 1
        count = Plants.query.filter(Plants.type.ilike('%' + keyword + '%')).count()
    else:
        for position in Position.query.filter(Position.area.ilike('%' + keyword + '%')).all():
            id_p = position.id
            plant = Plants.query.filter_by(id=id_p).first()
            picture = Picture.query.filter_by(id=id_p).first()
            dic = {'image': url_for('static', filename=picture.search_p),
                   'type': plant.type,
                   'name': plant.plant_name,
                   'area': position.area,
                   'time': plant.time,
                   'href': url_for('main.season', id=id_p),
                   'k': k}
            xianshi_t.append(dic)
            k = k + 1
        count = Position.query.filter(Position.area.ilike('%' + keyword + '%')).count()
    return render_template(
        'main/fenlei.html',
        xianshi=xianshi_t,
        form=form,
        count=count,
        k=k,
        form2=form2
    )


# index中跳转到“搜索”界面提交的表单
@main.route('/t1', methods=('GET', 'POST'))
def t1():
    form = Search()
    if form.validate_on_submit():
        if form.data['key'] == '':
            t = 'any'
        else:
            t = form.data['key']
        return redirect(url_for('main.search_2', keyword=t))
    return redirect(url_for('main.search_2', keyword='any'))


# index中跳转到“分类”网页提交的表单
@main.route('/t2', methods=('GET', 'POST'))
def t2():
    form2 = Fenlei()
    if form2.validate_on_submit():
        return redirect(url_for('main.fenlei', keyword=form2.data['key']))


# 选择季节
@main.route('/season/<id>', methods=('GET', 'POST'))
def season(id):
    form = Search()
    plant = Plants.query.filter_by(id=id).first()
    position = Position.query.filter_by(id=id).first()
    info = Info.query.filter_by(id=id).first()
    picture = Picture.query.filter_by(id=id).first()
    name_2 = plant.plant_name
    dic = {'name': plant.plant_name,
           'detail_p': url_for('static', filename=picture.detail_p),
           'academic': info.academic,
           'literary': info.literary,
           'time': plant.time,
           'language': plant.language,
           'longitude': position.longitude,
           'latitude': position.latitude}
    if plant.season == '春':
        tup = spring_style
    elif plant.season == '夏':
        tup = summer_style
    elif plant.season == '秋':
        tup = autumn_style
    else:  # 冬
        tup = winter_style
    return render_template(
        'main/detail.html',
        item=dic,
        form=form,
        k=name_2,
        style=Style(tup)
    )
