from run import db
import datetime
from history_meta import versioned_session, Versioned

class EmployeeModel(Versioned,db.Model):
    __tablename__ = 'employee'

    empid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=True)
    email = db.Column(db.String(120), nullable=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class AddressModel(Versioned,db.Model):
    __tablename__ = 'address'

    addid = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(120), nullable=True)
    state = db.Column(db.String(120), nullable=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

class ProductModel(Versioned,db.Model):
    __tablename__ = 'product'

    proid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=True)
    type = db.Column(db.String(120), nullable=True)
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()