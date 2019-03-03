from . import db


class CaModel():
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Author(db.Model, CaModel):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    birthyear = db.Column(db.String)
    deathyear = db.Column(db.String)

    def __repr__(self):
        return '<Author %s %s>' % (self.firstname, self.lastname)
