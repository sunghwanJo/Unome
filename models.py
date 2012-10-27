from unome import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column('user_id', db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    oauth_token = db.Column(db.String(200))
    oauth_secret = db.Column(db.String(200))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Users %r>'%self.name

class AnalyzedTable(db.Model):
    __tablename__ = 'analyzedTable'
    id = db.Column('analyzed_id', db.Integer, primary_key=True)
    key = db.Column(db.String(20))
    value = db.Column(db.String(200))

    def __init__(self, key, value)
        self.key = key
        self.value = value

    def __repr__(self)
        return '<Key : %s>'%self.key

