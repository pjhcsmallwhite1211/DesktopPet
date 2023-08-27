import random
from dataclasses import dataclass
from pprint import pprint

from PyQt5.QtCore import pyqtSignal, QObject, QThread
from PyQt5.QtGui import QCursor, QMouseEvent
from PyQt5.QtWidgets import QMainWindow
from loguru import logger
from PyQt5 import Qt, QtGui  # type: ignore # PyQt5 相关

import pet
import signalBin
import AI
import speak_box
from signalBin import pos, rect


class SpeakBox(object):
    def __init__(self, str, parent):
        self.mainWindow = QMainWindow()
        self.ui = speak_box.Ui_Form()
        self.ui.setupUi(self.mainWindow)
        self.parent = parent
        self.mainWindow.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.mainWindow.setAttribute(Qt.Qt.WA_TranslucentBackground)
        self.ui.text.setText(str)
        self.mainWindow.closeEvent = self.hide  # type: ignore
        self.ui.textEdit.textChanged.connect(
            lambda: self.input(self.ui.textEdit.text())
        )

    def getText(self):
        if "/end/" in self.ui.textEdit.text():
            return self.ui.textEdit.text().replace("/end/", "")
        return self.ui.textEdit.text()

    def input(self, text):
        if "/end/" in text:
            self.parent.speak(0, text=text.replace("/end/", ""))
            logger.info(f"type:{type(text)},text:{text}")
            return
        logger.info(f"type:{type(text)},text:{text}")

    def alignment(self):
        self.mainWindow.move(
            int(self.parent.nowPos.x),
            int(self.parent.nowPos.y - self.mainWindow.height()),
        )

    def show(self):
        self.alignment()
        self.mainWindow.show()

    def hide(self, a=0):
        self.mainWindow.hide()


class NLPthread(QThread):
    runNLP = pyqtSignal(dict)

    def __init__(self,task):
        super().__init__()
        self.isLive = True
        self.task = task

    def addTask(self, dict):
        self.task.append(dict)

    def run(self):
        if not self.task['parent'].generator.isOK:
            self.task['parent'].generator.init()
        result = self.task['parent'].generator.generateText(self.task["text"])
        self.task['parent'].returnSignal.emit(result[0]["text"])  # type: ignore

    def stop(self):
        self.isLive = False
        self.quit()
        self.wait()


class Pet(QObject):
    returnSignal = pyqtSignal(str)
    # moveSignal = pyqtSignal(str, int)
    changeStatusSignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.mainWindow = QMainWindow()
        self.ui = pet.Ui_Form()
        self.ui.setupUi(self.mainWindow)
        self.main = None
        signalBin.signalBin.getMain.emit(self)
        self.id = ["slime", "red", "orange", "yellow", "green", "blue", "purple"][len(self.main.pets)]  # type: ignore
        self.width = self.main.app.desktop().size().width()  # type: ignore
        self.height = self.main.app.desktop().size().height()  # type: ignore
        self.home = pos(0, 0)  # 固定在左上角的位置
        self.center = pos(int(self.width / 2), int(self.height / 2))  # 屏幕中心位置
        self.__bottom = pos(0, self.height - 120)  # 屏幕底部位置
        self.bottom_left = pos(0, self.height)
        self.bottom_right = pos(self.width, self.height)
        self.top_left = pos(0, 0)
        self.top_right = pos(self.width, 0)
        # 生成rect
        self.rect_bottom_left = rect(
            self.bottom_left.x,
            self.bottom_left.y - 180,
            self.bottom_left.x + 180,
            self.bottom_left.y,
        )
        self.rect_bottom_right = rect(
            self.bottom_right.x - 180,
            self.bottom_right.y - 180,
            self.bottom_right.x,
            self.bottom_right.y,
        )
        self.rect_top_left = rect(
            self.top_left.x,
            self.top_left.y,
            self.top_left.x + 180,
            self.top_left.y + 180,
        )
        self.rect_top_right = rect(
            self.top_right.x - 180,
            self.top_right.y,
            self.top_right.x,
            self.top_right.y + 180,
        )
        self.all = rect(0, 0, self.width, self.height)

        self.nowPos = pos(int(self.width / 2), int(self.height / 2))  # 当前位置

        self.mainWindow.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.mainWindow.setAttribute(Qt.Qt.WA_TranslucentBackground)
        self.ui.pet.setPixmap(
            QtGui.QPixmap(
                f"resources/image/{['icon.png', 'icon1.png', 'icon2.png', 'icon3.png', 'icon4.png', 'icon5.png', 'icon6.png'][len(self.main.pets)]}"
                # type: ignore
            )
        )  # type: ignore # type: ignore
        self.face = "face_happy"
        self.feet = "foot_stand"
        self.mainWindow.show()
        self.setMouseEvent()
        self.active = True
        self.speed = 5
        self.initAI()
        self.now_status = "stand"
        # 创建屏幕角落的坐标
        self.speakBox = SpeakBox("hello /end/", self)
        self.isSpeaking = False
        self.logicTaskList=[]
        self.changeStatusSignal.connect(self.changeStatus)
    def __str__(self):
        return f"<pet id={self.id},active={self.active},now_status={self.now_status}>"
    def __repr__(self):
        return self.__str__()

    def changeStatus(self, status):
        self.now_status = status
        self.logicTaskList.extend(self.getLogic())


    def changeItem(self, item):
        """
        切换 item 图片
        """

        self.ui.item.setPixmap(QtGui.QPixmap(f":/image/image/{item}"))  # 切换 item 图片

    def updataFace(self):
        self.ui.face.setPixmap(QtGui.QPixmap(f"resources/image/{self.face}.png"))

    def setFace(self, face):
        self.face = face
        self.updataFace()

    def updataFeet(self):
        self.ui.feet.setPixmap(QtGui.QPixmap(f"resources/image/{self.feet}.png"))

    def setFeet(self, feet):
        self.feet = feet
        self.updataFeet()

    def mainWindow_re__mousePressEvent(self, event: QMouseEvent = None):  # type: ignore
        # logger.info(f"mainWindow_re__mousePressEvent running--- {self.id}")
        #
        self.mouseButtonDown = True
        self.mousePos_toWindow = pos(event.pos().x(), event.pos().y())
        self.setFace("face___")
        #
        # logger.info(
        #     f"{self.id} mouseButtonDown changed: {self.mouseButtonDown}, mousePos_toWindow changed: {pos(event.pos().x(), event.pos().y())}\n"
        # )

    def mainWindow_re__mouseReleaseEvent(self, event: QMouseEvent = None):
        # logger.info(f"mainWindow_re__mouseReleaseEvent running--- {self.id}")
        #
        self.mouseButtonDown = False
        self.mousePos_toWindow = signalBin.pos(0, 0)
        pos = QCursor.pos()
        self.nowPos = signalBin.pos(
            pos.x() - self.mousePos_toWindow.x, pos.y() - self.mousePos_toWindow.y
        )
        self.setFace("face_happy")

        # logger.info(f"{self.id} mouseButtonDown changed: {self.mouseButtonDown}\n")

    def mainWindow_re__mouseMoveEvent(self, event):
        # logger.info(f"mainWindow_re__mouseMoveEvent running--- {self.id}")
        #
        self.mouseButtonDown = False
        pos = QCursor.pos()
        window_pos = self.mousePos_toWindow
        # logger.info(f"mouse pos: ({pos.x()}, {pos.y()}) id: {self.id}")
        # logger.info(f"mouse pos window: ({window_pos.x}, {window_pos.y}) id: {self.id}")
        # logger.info(
        #     f"mouse pos move to: ({pos.x() - window_pos.x}, {pos.y() - window_pos.y}) id: {self.id}"
        # )
        self.moveMainWindow(signalBin.pos(pos.x() - window_pos.x, pos.y() - window_pos.y))

        # logger.info(f"{self.id} mouseButtonDown changed: {self.mouseButtonDown}\n")

    def setMouseEvent(self):
        logger.info(f"setMouseEvent running--- {self.id}")
        self.mousePos_toWindow = pos(0, 0)
        self.mainWindow.mousePressEvent = self.mainWindow_re__mousePressEvent  # type: ignore
        self.mainWindow.mouseMoveEvent = self.mainWindow_re__mouseMoveEvent  # type: ignore
        self.mainWindow.mouseReleaseEvent = self.mainWindow_re__mouseReleaseEvent  # type: ignore
        logger.info("\n")

    def hide(self):
        logger.info(f"{self.id} hide")
        self.mainWindow.hide()
        self.speakBox.hide()
        self.active = False

    def show(self):
        logger.info(f"{self.id} show")
        self.mainWindow.show()
        self.speakBox.show()
        self.active = True

    def moveMainWindow(self, pos):
        # logger.info(f"moveMainWindow running --- {self.id}, move to: {pos}, time: {time.time()}")
        logger.info(f"{type(pos.x)},{type(pos.y)},{int(pos.x)},{int(pos.y)}")
        self.mainWindow.move(int(pos.x), int(pos.y))
        self.nowPos = signalBin.pos(pos.x, pos.y)
        # logger.info(f"\n time: {time.time()}")

    #
    # def walkFlash(self, var):  #############################################
    #     if var % 5 == 0:
    #         self.setFeet("foot_right")
    #         self.ui.feet.repaint()
    #     elif var % 5 == 3:
    #         self.setFeet("foot_left")
    #         self.ui.feet.repaint()
    #
    # def moveStep(self, direction, distance, command):  #########################################
    #     # logger.info(
    #     #     f"""moveStep running --- {self.id}:
    #     #             direction: {direction},
    #     #             distance: {distance}
    #     #             cycle:{self.speed * distance},
    #     #             Δ_plus:{1 / self.speed},
    #     #             time: {time.time()},
    #     #             speed:  {self.speed},
    #     #             nowPos: {self.nowPos},
    #     #             height: {self.height},
    #     #             width: {self.width},
    #     #             status: {self.now_status},
    #     #             command: {command}
    #     #
    #     #
    #     #     """)
    #     aStep = 0
    #
    #     direction_dict = {
    #         "north": (0, -1 / self.speed),
    #         "south": (0, 1 / self.speed),
    #         "east": (1 / self.speed, 0),
    #         "west": (-1 / self.speed, 0),
    #     }
    #     for i in range(int(self.speed * distance)):
    #         self.nowPos.x += direction_dict[direction][0]
    #         self.nowPos.y += direction_dict[direction][1]
    #         self.nowPos.x = round(self.nowPos.x, 1)
    #         self.nowPos.y = round(self.nowPos.y, 1)
    #
    #         aStep += 1
    #         # time.sleep(0.000001)
    #         self.moveMainWindow(self.nowPos)
    #         self.walkFlash(aStep)
    #     # logger.info(
    #     #     f"aStep:{aStep},move:{(direction_dict[direction][0] * aStep, direction_dict[direction][1] * aStep)},change:{aStep // 5}")
    #
    #     if not self.inRect(self.all):
    #         logger.error("move out")
    #         logger.error(
    #             f"nowPos:{self.nowPos},Δx:{1920 - self.nowPos.x},Δy:{self.nowPos.y}"
    #         )
    #         raise Exception(f"Out of range")

    def bottomPosUpdate(self):
        self.__bottom = pos(self.nowPos.x, self.height - 120)
        return self.__bottom

    def inRect(self, rect):
        # logger.info(f"""
        #     inRect running --- {self.id}, {rect}:
        #         rect.left_top_x: {rect.left_top_x},
        #         self.nowPos.x: {self.nowPos.x},
        #         rect.right_bottom_x: {rect.right_bottom_x},
        #         rect.left_top_y: {rect.left_top_y},
        #         self.nowPos.y: {self.nowPos.y},
        #         rect.right_bottom_y: {rect.right_bottom_y}
        #         rect.id: {id(rect)}
        #         self.all.id: {id(self.all)},
        #         self.rect_top_right.id: {id(self.rect_top_right)},
        #         self.rect_bottom_left.id: {id(self.rect_bottom_left)}
        #         self.rect_top_left.id: {id(self.rect_top_right)}
        #         self.rect_bottom_right.id: {id(self.rect_bottom_right)}
        # """)
        # logger.info(f"""
        #         rect.left_top_x <= self.nowPos.x <= rect.right_bottom_x 的值: {rect.left_top_x <= self.nowPos.x <= rect.right_bottom_x},
        #         rect.left_top_y <= self.nowPos.y <= rect.right_bottom_y 的值: {rect.left_top_y <= self.nowPos.y <= rect.right_bottom_y}
        # """)
        logger.warning("in rect")
        if (
                rect.left_top_x <= self.nowPos.x <= rect.right_bottom_x
                and rect.left_top_y <= self.nowPos.y <= rect.right_bottom_y
        ):
            return True
        return False

    # def walk(self, actuator):
    #     self.main.MoveThread.addLogic.emit(self.getLogic())

    def getLogic(self):
        if self.now_status == "playMode":
            logger.debug(f"playing mode,{self.now_status}")
            return signalBin.changeTo_move_step(signalBin.logic_move_to_endpoint(self,pos(random.randint(0, self.width), random.randint(0, self.height)),3.0))

        elif self.now_status == "stand":
            logger.debug(f"standing still,{self.now_status}")
            if not self.inRect(self.rect_bottom_left) or self.inRect(
                    self.rect_bottom_right
            ):
                return  signalBin.changeTo_move_step(signalBin.logic_move_to_endpoint(self,random.choice([pos(0, self.height - 50 - 120), pos(self.width - 120, self.height - 50 - 120)]),3.0))

        elif self.now_status == "workingMode":
            logger.debug(f"working mode,{self.now_status}")
            if self.inRect(self.rect_bottom_left):
                return signalBin.changeTo_move_step(signalBin.logic_move_to_endpoint(self,random.choice([pos(random.randint(0, self.width - 120), self.height - 50 - 120),
                                   pos(0, random.randint(0, self.height - 50 - 120))]),3.0))
            elif self.inRect(self.rect_bottom_right):
                return signalBin.changeTo_move_step(signalBin.logic_move_to_endpoint(self, random.choice([pos(random.randint(0, self.width - 120), self.height - 50 - 120),
                                   pos(self.width - 120, random.randint(0, self.height - 50 - 120))]),3.0))
            elif self.inRect(self.rect_top_left) or self.inRect(self.rect_top_right):
                return [signalBin.logic_move_step(self,random.randint(
                        int((self.height - self.nowPos.y) - 50 - 120),
                        int((self.height - self.nowPos.y) - 120),
                    ),"south",3.0)]
            else:
                return signalBin.changeTo_move_step(signalBin.logic_move_to_endpoint(self, random.choice([pos(0, self.height - 50 - 120), pos(self.width - 120, self.height - 50 - 120)]),3.0))
        elif self.now_status == "stop":
            pass

    def move(self, direction, speed):
        logger.debug(f"moving {self.id}")

        direction_dict = {
            "north": (0, -speed),
            "south": (0, speed),
            "east": (speed, 0),
            "west": (-speed, 0),
        }
        self.nowPos.x += direction_dict[direction][0]
        self.nowPos.y += direction_dict[direction][1]

        self.nowPos.x = round(self.nowPos.x, 1)
        self.nowPos.y = round(self.nowPos.y, 1)
        self.moveMainWindow(self.nowPos)
        self.setFeet(random.choice(["foot_left", "foot_right"]))
        self.speakBox.alignment()

        if not self.inRect(self.all):
            logger.error("move out")
            logger.error(
                f"nowPos:{self.nowPos},Δx:{1920 - self.nowPos.x},Δy:{self.nowPos.y}"
            )
            raise Exception(f"Out of range")
        logger.debug(f"moving {self.id}")
    #
    # def walk_condition(self, actuator):
    #     if random.randint(0, 10) == 0:
    #         return True
    #
    # def speak_condition(self, actuator):
    #     if random.randint(0, 50) == 0 and not self.isSpeaking:  # type: ignore
    #         return True
    #
    def speak(self, actuator, **text):
        if text == {}:
            text["text"] = self.speakBox.getText()
        logger.info(f"{self.id} speaking,text:{text}")
        self.isSpeaking = True
        # self.threadSpeak = self.main.threadPool.submit(self.main.generator.generateText, self,"hello")
        self.main.NLPthread.runNLP.emit({'parent':self,'text':text["text"]})  # type: ignore

    def speak_UI(self, str):
        logger.info(f"{self.id} speak_UI,\033[7;44m{str}\033[0m")
        self.speakBox.ui.text.setText(str)
        self.speakBox.show()
    def doTask(self):
        logger.debug(f"{self.id} doTask")
        pprint(self.logicTaskList)
        if self.logicTaskList:
            logic = self.logicTaskList[0]
            if logic.type=="move_step":
                if logic.speed > logic.distance:
                    self.move(logic.direction, logic.distance)
                else:
                    self.move(logic.direction, logic.speed)
                    self.logicTaskList.remove(logic)
    def doTask_condition(self):
        return self.active
    def initAI(self):
        logger.info(f"{self.id} initAI running")
        self.main.eventList.append(signalBin.Func(self.doTask,self,self.doTask_condition,f"{self.id}.doTask"))
        # self.AI = AI.AI(self)
        # self.AI.add(AI.Actuators(self.walk, self.walk_condition, self.AI))
        # self.AI.add(AI.Actuators(self.speak, self.speak_condition, self.AI))
        # self.main.timerThread.setTimerFuncs.emit(signalBin.Func(self.AI.makeDecisions, self), "add")
        self.generator=AI.generator(self)
        self.returnSignal.connect(self.speak_UI)
