# -*- coding: utf-8 -*-
import os.path, jpype

jarpath = os.path.join(os.path.abspath('.'), 'jhannanum.jar')
jpype.startJVM(jpype.getDefaultJVMPath(),"-ea","-Djava.class.path=%s"%jarpath)


WorkflowCls = jpype.JClass('kr.ac.kaist.swrc.jhannanum.hannanum.Workflow')
WorkflowFactoryCls = jpype.JClass('kr.ac.kaist.swrc.jhannanum.hannanum.WorkflowFactory')


class WorkflowMorphAnalyzer:
    operation_flag = False
    workflow = WorkflowFactoryCls.getPredefinedWorkflow(WorkflowFactoryCls.WORKFLOW_MORPH_ANALYZER)

    def operation_analyzer(self):  
        try:
            self.workflow.activateWorkflow(True)
            self.operation_flag = True
            print 'analyze start'
        except :
            print 'exception !!'
            exit()

    def exit_analyzer(self):
        self.operation_flag = False
        self.workflow.close()

    def request_analyze(self,plaintext):
        if self.operation_flag == True:
            self.workflow.analyze(plaintext)
            return self.workflow.getResultOfDocument()
        else:
            return -1 

    def __get_operation_flag(self):
        return self.operation_flag


