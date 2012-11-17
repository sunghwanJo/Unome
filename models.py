from flask.ext.sqlalchemy import SQLAlchemy
from unome import app

db = SQLAlchemy(app)

class EmotionTable(db.Model):
    __tablename__ = 'EmotionTable'
    id = db.Column('analyzed_id', db.Integer, primary_key=True)
    emotion = db.Column(db.String(10))
    value = db.Column(db.String(20))

    def __init__(self, emotion, value):
        self.emotion = emotion
        self.value = value

    def __repr__(self):
        return '<Emotion : %s>'%self.emotion
