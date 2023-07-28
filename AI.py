import time
from loguru import logger

from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer, GPT2LMHeadModel, GPT2Tokenizer

import signalBin


class generator(object):

    def __init__(self):
        pass

    def init(self):
        self.model_name = "Helsinki-NLP/opus-mt-en-zh"
        self.model_translator = AutoModelForSeq2SeqLM.from_pretrained(self.model_name,
                                                                      cache_dir='D:\\Desktop\\python\\huggingface_cache')
        self.tokenizer_translator = AutoTokenizer.from_pretrained(self.model_name,
                                                                  cache_dir='D:\\Desktop\\python\\huggingface_cache')

        # 选择模型和分词器
        self.model = GPT2LMHeadModel.from_pretrained("gpt2", cache_dir='D:\\Desktop\\python\\huggingface_cache')
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2", cache_dir='D:\\Desktop\\python\\huggingface_cache')

        # 创建生成器和翻译器的pipeline
        self.generator = pipeline("text-generation", model=self.model, tokenizer=self.tokenizer)
        self.translator = pipeline("translation_en_to_zh", model=self.model_translator,
                                   tokenizer=self.tokenizer_translator)

    def generateText(self, prompt="creat a 'dict' with python.tell me how to write it"):
        print("s")
        # 设置生成随机文本的提示
        prompt = prompt

        # 使用生成器生成随机文本（英文）
        output_text = self.generator(prompt, max_length=400, num_return_sequences=1, do_sample=True)[0][
            'generated_text']

        # 将换行符替换为特殊字符<n>
        output_text = output_text.replace('\n', '<n>')

        # 将随机文本翻译成中文,并设置换行
        translated_text = self.translator([output_text], max_length=400)[0]['translation_text']

        # 打印生成的随机文本（英文版本）
        print(f"Generated Text (in English): {output_text}")

        # 打印翻译后的随机文本（中文版本）
        print(f"\nTranslated Text (in Chinese): {translated_text}")


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
