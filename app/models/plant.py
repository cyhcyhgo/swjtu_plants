from app.extensions import db


class Plants(db.Model):
    __tablename__ = 'Plants'
    # 每个属性定义一个字段
    id = db.Column(db.Integer, primary_key=True)
    plant_name = db.Column(db.String(10), unique=True)
    time = db.Column(db.String(10))
    language = db.Column(db.String(50))
    type = db.Column(db.String(15))
    family = db.Column(db.String(15))
    season = db.Column(db.String(10))
    info = db.relationship('Info', backref='Plants', uselist=False)
    position = db.relationship('Position', backref='Plants', uselist=False)
    picture = db.relationship('Picture', backref='Plants', uselist=False)

    def __repr__(self):
        return '<Plants %r>' % self.plant_name


class Info(db.Model):
    __tablename__ = 'Info'
    # 每个属性定义一个字段
    id = db.Column(db.Integer, primary_key=True)
    academic = db.Column(db.String(500))
    literary = db.Column(db.String(500))
    brief = db.Column(db.String(500))
    plants_id = db.Column(db.Integer, db.ForeignKey('Plants.id'))

    def __repr__(self):
        return '<Info %r>' % self.id


class Position(db.Model):
    __tablename__ = 'Position'
    # 每个属性定义一个字段
    id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    area = db.Column(db.String(30))
    plants_id = db.Column(db.Integer, db.ForeignKey('Plants.id'))

    def __repr__(self):
        return '<Position %r>' % self.id


class Picture(db.Model):
    __tablename__ = 'Picture'
    # 每个属性定义一个字段
    id = db.Column(db.Integer, primary_key=True)
    search_p = db.Column(db.String(40))
    detail_p = db.Column(db.String(40))
    plants_id = db.Column(db.Integer, db.ForeignKey('Plants.id'))

    def __repr__(self):
        return '<Picture %r>' % self.id

