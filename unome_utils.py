# -*- coding:utf-8 -*-
import os.path, sys
reload(sys)

sys.setdefaultencoding('utf-8')
pyhannanumPath = os.path.join(os.path.abspath('.'),'pyhannanum')
sys.path.append(pyhannanumPath)

from pynanum import WorkflowMorphAnalyzer


class TweetAnalyzer(WorkflowMorphAnalyzer):
    strdic={}
    def __init__(self):
        WorkflowMorphAnalyzer.__init__(self)

    def analyze_tweet(self, string):
        if self._get_operation_flag() == False:
            exit()
        
        seperated_list = self.request_analyze(string).split('\n')
        for word in seperated_list:
            word = word.replace('\n', '')
            if not len(word):
                pass
            elif word.find('\t'):
                parent = word
                self.strdic[parent] = []
            else:
                self.strdic[parent].append(word.replace('\t', ''))
        print self.strdic                          
