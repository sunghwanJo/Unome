# -*- coding:utf-8 -*-
import pynanum, sys
reload(sys)
sys.setdefaultencoding('utf-8')

analyzer =  pynanum.WorkflowMorphAnalyzer()

analyzer.operation_analyzer()
print analyzer.request_analyze('안녕 하세요 저는 조성환입니다.')


