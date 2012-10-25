# -*- coding:utf-8 -*-
import os.path, jpype

jarpath = os.path.join(os.path.abspath('.'), 'jhannanum.jar')
jpype.startJVM(jpype.getDefaultJVMPath(),"-ea","-Djava.class.path=%s"%jarpath)


WorkflowCls = jpype.JClass('kr.ac.kaist.swrc.jhannanum.hannanum.Workflow')
WorkflowFactoryCls = jpype.JClass('kr.ac.kaist.swrc.jhannanum.hannanum.WorkflowFactory')


class WorkflowMorphAnalyzer:
    def __init__(self):  
        try:
            self.workflow = WorkflowFactoryCls.getPredefinedWorkflow(WorkflowFactoryCls.WORKFLOW_MORPH_ANALYZER)
            self.workflow.activateWorkflow(True)
            self.operation_flag = True
            print 'analyze start'
        except :
            self.operation_flag = False
            print 'exception !!'

    def exit_analyzer(self):
        self.operation_flag = False
        self.workflow.close()

    def request_analyze(self,plaintext):
        if self.operation_flag == True:
            self.workflow.analyze(plaintext)
            return self.workflow.getResultOfDocument()
        else:
            return -1 

    def _get_operation_flag(self):
        return self.operation_flag


