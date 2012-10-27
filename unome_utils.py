# -*- coding:utf-8 -*-
import os.path, sys
reload(sys)

sys.setdefaultencoding('utf-8')
pyhannanumPath = os.path.join(os.path.abspath('.'),'pyhannanum')
sys.path.append(pyhannanumPath)

from pynanum import WorkflowMorphAnalyzer
from models import AnalyzedTable
from unome import db

class TweetAnalyzer(WorkflowMorphAnalyzer):
    def __init__(self):
        WorkflowMorphAnalyzer.__init__(self)

    def update_analyzed_table(self, string):
        analyzed_dict = {}
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
            analyzedTable =AnalyzedTable(key,analyzed_dict[key] )
            db.session.add(analyzedTable)

        db.session.commit()
        return True   

   ##analyzed_dict를 init하는놈 추가
    def init_analyzed_dict(self):
         pass

   ## analyzed_dict를 backup 하는놈 추가
    def save_to_db_analyzed_dict(self):
        pass
    # analyzed_dict에서 적당한 값 찾기 -> 점수내기 -> 반영하기

    def search_data():
        pass

    def _get_analyzed_dict(self):
        return self.analyzed_dict
