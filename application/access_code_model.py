from application import db

class AccessCode(db.Model):
    __tablename__ = "access_code"
    id = db.Column(db.Integer, primary_key=True)
    access_code = db.Column(db.String(10), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    user_type = db.Column(db.String(64))

    def __repr__(self):
        return '<AccessCode {}>'.format(self.access_code)
