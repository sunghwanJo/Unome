import os.path, sys

pyhannanumPath = os.path.join(os.path.abspath('.'),'pyhannanum')
sys.path.append(pyhannanumPath)

import pynanum


analyzer = WorkflowMorphAnalyzer()

analyzer.operation_analyzer()

def analyze_tweet():
    pass
