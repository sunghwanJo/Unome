# -*- coding:utf-8 -*-
import os.path, sys
reload(sys)

sys.setdefaultencoding('utf-8')
pyhannanumPath = os.path.join(os.path.abspath('.'),'pyhannanum')
sys.path.append(pyhannanumPath)

from pynanum import WorkflowMorphAnalyzer


class TweetAnalyzer(WorkflowMorphAnalyzer):
    analyzed_dict={}
    def __init__(self):
        WorkflowMorphAnalyzer.__init__(self)

    def update_analyzed_dict(self, string):
        if self._get_operation_flag() == False:
            return False
        
        string_index_list = string.split(' ')
        
        seperated_list = self.request_analyze(string).split('\n')
        for word in seperated_list:
            word = word.replace('\n', '')
            if not len(word):
                pass
            elif word.find('\t'):
                parent_node = word
                self.analyzed_dict[parent_node] = []
            else:
                self.analyzed_dict[parent_node].append(word.replace('\t', ''))
        return self.analyzed_dict
    
   
    def _get_analyzed_dict(self):
        return self.analyzed_dict

