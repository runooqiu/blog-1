from app import db

class User(db.Model):
    __table_name__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(80), nullable=False)
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    def __str__(self):
        return self.username

    def __repr__(self):
        return "<%s>" % self
