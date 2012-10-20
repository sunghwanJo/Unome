import os.path, sys

pyhannanumPath = os.path.join(os.path.abspath('.'),'pyhannanum')
sys.path.append(pyhannanumPath)

import pynanum


def analyzer_init():
    analyzer = WorkflowMorphAnalyzer()
    analyzer.operation_analyzer()

def analyze_tweet():
    if analyzer.__get_operation_flag() == True:
        pass

    
