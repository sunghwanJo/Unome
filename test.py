# -*- coding:utf-8 -*-
import jhannanum, sys
reload(sys)
sys.setdefaultencoding('utf-8')
analyzer =  jhannanum.WorkflowMorphAnalyzer()

analyzer.operation_analyzer()
analyzer.request_analyze('안녕 하세요 저는 조성환입니다.')
analyzer.request_analyze('Fuck you man')

