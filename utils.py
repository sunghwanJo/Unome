from models import db, EmotionTable, NegativeTable
import unome


class Utils(): 
    def db_create(self):
        db.create_all()
    
    def add_emotion_object(self, emotion, value):
        if emotion and value :
            print 'dont Suffice arguments'
        
        emotion_object = EmotionObject(emotion, value)
        db.session.add(emotion_object)
        db.session.commit()

   
   def add_negative_object(self, negative_word):
        if negative_word:
            print 'dont Suffice arguments'

        negative_object = NegativeObject(negative_word)
        db.session.add(emotion_oject)
        db.session.commit()



    def db_refresh(self):
        DB_URI = unome.app.config['SQLALCHEMY_DATABASE_URI'].split(':///')[1]
        command = 'rm %s'%(DB_URI)

        self.db_create()


        

