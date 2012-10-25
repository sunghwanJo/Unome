# -*- coding:utf-8 -*-
import pynanum, sys


reload(sys)
sys.setdefaultencoding('utf-8')

analyzer =  pynanum.WorkflowMorphAnalyzer()
analyzer.operation_analyzer()

#f = file('unome.log')

#f.write(analyzer.request_analyze('안녕 하세요 저는 조성환입니다.'))
"""
strdic = {}
for line in f.readlines():
    line = line.replace('\n', '').replace('\t', '[TAB]')
    if not len(line):
        pass
    elif line.find('[TAB]'):
        parent = line
        strdic[parent] = []  
    else:
        strdic[parent].append(line.replace('[TAB]', ''))

for i in strdic.keys():
    print i
    for j in strdic[i]:
        print "\t%s"%(j)
"""

print analyzer.request_analyze('안녕 하세요 저는 조성환입니다.').split('\n')


f.close()

