from PyQt5.QtCore import pyqtSignal, QObject, QThread

from loguru import logger

from transformers import pipeline

class Generator(object):

    def __init__(self):
        self.isOK=False
    def init(self):
        self.model = 'gpt2'
        self._generateText = pipeline("text-generation", model=self.model)  # 文本生成
        logger.warning("generator \033[96minited\033[0m~~~~~~~~~~~~~~~~~~~~~")
        self.isOK=True
    def generateText(self,prompt):
        if not self.isOK:
            self.init()
        result=self._generateText(prompt)
        # parent.returnSignal.emit(result[0]['generated_text'])
        return result[0]['generated_text'] # type: ignore
class NLPSystem(object):
    def __init__(self):
        self.NLPTasks=[]
        self.generator=Generator()
        self.generator.init()
    def NLPTaskFinish(self,obj):
        self.NLPTasks.remove(obj)
    def addNLPTask(self,taskStr,returnSignal,generator=None):
        logger.debug(self.NLPTasks)
        if self.NLPTasks!=[]:
            return
        if generator == None:
            generator=self.generator
        task=NLPThread(taskStr,returnSignal,generator)
        task.finishSignal.connect(self.NLPTaskFinish)
        self.NLPTasks.append(task)
        task.start()
class NLPThread(QThread):
    finishSignal = pyqtSignal(object)
    def __init__(self,task,returnSignal,generator):
        super(NLPThread, self).__init__()
        self.isInit=False
        self.isAlive = True
        self.task = task
        self.returnSignal = returnSignal
        self.generator = generator
    def run(self):  
        result=self.generator.generateText(self.task)
        self.returnSignal.emit(result)
        self.finishSignal.emit(self)
nlpSystem=NLPSystem()
