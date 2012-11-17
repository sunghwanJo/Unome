# -*- coding:utf-8 -*-
import os.path, sys
reload(sys)

sys.setdefaultencoding('utf-8')
pyhannanumPath = os.path.join(os.path.abspath('.'),'pyhannanum')
sys.path.append(pyhannanumPath)

from pynanum import WorkflowMorphAnalyzer
from models import EmotionTable, db

class TweetAnalyzer(WorkflowMorphAnalyzer):
    def __init__(self):
        WorkflowMorphAnalyzer.__init__(self)

    def get_emotion_data(self, string):
        analyzed_table = {}
        
        if self._get_operation_flag() == False:
            return False
        string_sequence = string.split(' ')
        seperated_list = self.request_analyze(string).split('\n')
        
        for word in seperated_list:
            word = word.replace('\n', '')
            if not len(word):
                pass
            elif word.find('\t'):
                parent_node = word
                analyzed_table[parent_node] = []
            else:
                analyzed_table[parent_node].append(word.replace('\t', ''))
            
        for key in analyzed_table.keys():
            for value in analyzed_table[key]:
                emotion = self.compare_with_emotiontable(value)
                #감정을 찾으면?  string_sequence.index(key), emotion
                if emotion:  
                    print emotion, string_sequence.index(key), key


                    break  # analyzed_table[key]의 첫번째  value만 탐색i

        return True


    def add_emotion_data(self, emotion, value):
        emotiontable = EmotionTable(unicode(emotion), unicode(value))
        db.session.add(emotiontable)
        db.session.commit()

    def compare_with_emotiontable(self, value):
        emotion_table = EmotionTable.query.all()
        emotion = ''
        for emotion_object in emotion_table:
            if emotion_object.value in value:
                emotion = emotion_object.emotion
                break
        if emotion:
            return emotion

        return False


    def compare_with_amptable(self, value):
        amp_point = 1
        return amp_point

    def compare_with_changetable(self, value):
        change_flag = 1

        return change_flag


    



