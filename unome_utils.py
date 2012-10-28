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

    def get_emotion_point(self, string):
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
                if emotion:
                    print emotion, string_sequence.index(key), key
                    break  # analyzed_table[key]의 첫번째  value만 탐색i

        return True


    def add_emotion_data(self, emotion, value):
        emotiontable = EmotionTable(emotion, unicode(value))
        db.session.add(emotiontable)
        db.session.commit()

    def compare_with_emotiontable(self, word):
        emotion_table = EmotionTable.query.all()
        emotion = ''
        for emotion_object in emotion_table:
            if emotion_object.value in word:
                emotion = emotion_object.emotion
                break
        if emotion:
            return emotion

        return False


    def compare_with_amptable(self, word):
        amp_point = 1
        return amp_point

    def compare_with_changetable(self, word):
        change_flag = False
        return change_flag



