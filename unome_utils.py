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

        
        for key in analyzed_dict.keys():
            analyzed_dict[key]


        return True   


    def add_emotion_data(self, emotion, value):
        emotiontable = EmotionTable(emotion, unicode(value))
        db.session.add(emotiontable)
        db.session.commit()

    def compare_with_emotiontable(self, word):
        emotion = EmotionTable.query.filter_by(value=unicode(word)).first().emotion
        return emotion

    def compare_with_amptable(self, word):
        amp_point = 0
        return amp_point

    def compare_with_changetable(self, word):
        change_flag = False
        return change_flag
