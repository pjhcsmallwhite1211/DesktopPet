import time
from PyQt5.QtCore import pyqtSignal

from loguru import logger

from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer, GPT2LMHeadModel, GPT2Tokenizer

import signalBin


class generator(object):

    def __init__(self,main):
        self.main = main

    def init(self):
        self.model = 'gpt2'
        self._generateText = pipeline("text-generation", model=self.model)  # 文本生成
        logger.warning("generator \033[96minited\033[0m~~~~~~~~~~~~~~~~~~~~~")
        self.main.isGeneratorOK=True
    def generateText(self,parent,prompt):
        result=self._generateText(prompt)
        # parent.returnSignal.emit(result[0]['generated_text'])
        parent.isSpeaking=False
        return result[0]['generated_text']
    # def generateText(self, parent, prompt="creat a 'dict' with python.tell me how to write it"):
    #     logger.debug("s")
    #     try:
    #         # 设置生成随机文本的提示
    #         prompt = prompt
    #         logger.warning("1")
    #         # 使用生成器生成随机文本（英文）
    #         output_text = self.generator(prompt, max_length=400, num_return_sequences=1, do_sample=True)[0][
    #             'generated_text']
    #         logger.warning("2")
    #         # 将换行符替换为特殊字符<n>
    #         output_text = output_text.replace('\n', '<n>')
    #         logger.warning("3")
    #         # 将随机文本翻译成中文,并设置换行
    #         translated_text = self.translator([output_text], max_length=400)[0]['translation_text']
    #         logger.warning("4")
    #         # 打印生成的随机文本（英文版本）
    #         logger.debug(f"Generated Text (in English): {output_text}")
    #         logger.warning("5")
    #         # 打印翻译后的随机文本（中文版本）
    #         logger.debug(f"\nTranslated Text (in Chinese): {translated_text}")
    #         parent.returnSignal.emit(translated_text)
    #         parent.isSpeaking=False
    #     except Exception as e:
    #         raise e


class AI(object):
    def __init__(self, parent):
        self.main = None
        signalBin.signalBin.getMain.emit(self)
        self.parent = parent
        self.actuatorList = []
        self.id = self.parent.id + f"_AI"
        logger.info(f"{self.parent.id}'s AI init")
        logger.info("infos:")
        logger.info(f"    -id: {self.id}")

    def add(self, actuator):
        self.actuatorList.append(actuator)
        return len(self.actuatorList) - 1

    def makeDecisions(self):
        # logger.info(f"makeDecisions runnning--- {self.id} time: {time.time()}")
        for actuators in self.actuatorList:
            actuators.run()
        # logger.info(f"makeDecisions done--- {self.id} time: {time.time()}")


class Actuators(object):  # 执行器
    def __init__(self, action, condition, parent: AI):
        self.action = action
        self.condition = condition
        self.parent = parent
        self.id = self.parent.id + f"_Actuators{len(self.parent.actuatorList)}"

    def run(self):
        if self.condition(self):
            self.action(self)
