# -*- coding:utf-8 -*-
import os.path, sys
reload(sys)

sys.setdefaultencoding('utf-8')
pyhannanumPath = os.path.join(os.path.abspath('.'),'pyhannanum')
sys.path.append(pyhannanumPath)

from pynanum import WorkflowMorphAnalyzer
from models import EmotionTable
"""
def add_emotion_data(self, emotion, value):
    emotiontable = EmotionTable(unicode(emotion), unicode(value))
    db.session.add(emotiontable)
    db.session.commit()
"""
class EmotionAnalyzer(WorkflowMorphAnalyzer):
    emotion_table = ''

    def __init__(self):
        WorkflowMorphAnalyzer.__init__(self)
        self.emotion_table = EmotionTable.query.all()

    def get_emotion_data(self, string):
        
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
        
        emotion             = {}
        emotion[index]      = -1
        emotion[point]      = 1
        emotion[value]      = ''

        for key in analyzed_table.keys():
            for value in analyzed_table[key]:
                emotion[value] = self.get_emotion(value)
                if emotion:
                    emotion[index] = string_sequence.index(key)
                    break                 
                amp_point = self.get_amp_point(value)
                negative_flag = self.get_negative_flag(value)
                

        emotion[point] = amp_point*negative_flag
                
        return emotion

    def get_emotion(self, value):
        emotion = ''
        for emotion_object in self.emotion_table:
            if emotion_object.value in value:
                emotion = emotion_object.emotion
                break
        if emotion:
            return emotion

        return False


    def get_amp_point(self, value):
        amp_point = 1
        return amp_point

    def get_negative_flag(self, value):
        negative_flag = 1

        return negative_flag

