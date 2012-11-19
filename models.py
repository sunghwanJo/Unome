from flask.ext.sqlalchemy import SQLAlchemy
import unome

db = SQLAlchemy(unome.app)

class EmotionTable(db.Model):
    __tablename__ = 'EmotionTable'
    id = db.Column('emotion_id', db.Integer, primary_key=True)
    emotion = db.Column(db.String(10))
    value = db.Column(db.String(20))

    def __init__(self, emotion, value):
        self.emotion = emotion
        self.value = value

    def __repr__(self):
        return '<Emotion : %s>'%self.emotion

class NegativeTable(db.Model):
    __tablename__ = 'NegativeTable'
    id = db.Column('negative_id', db.Integer, primary_key=True)
    negative_word = db.Column(db.String(10))

    def __init__(self, negative_word, value):
        self.negative_word = negative_word
        self.value = value

    def __repr__(self):
        return '<NegativeWord : %s>'%self.negative_word



"""
def add_emotion_data(self, emotion, value):
    emotiontable = EmotionTable(unicode(emotion), unicode(value))
    db.session.add(emotiontable)
    db.session.commit()
"""
