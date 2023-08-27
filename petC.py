from pprint import pprint
import sys
import time
from PyQt5.QtCore import pyqtSignal, QObject, QThread
from PyQt5.QtGui import QCursor, QMouseEvent
from PyQt5.QtWidgets import QMainWindow
from loguru import logger
from PyQt5 import Qt, QtGui  # type: ignore # PyQt5 相关
import pet
from libs import *
from NLP import *

class Pet(QObject):
    returnSignal=pyqtSignal(str)
    def __init__(self, id, num,):
        super().__init__()
        # cache
        self.mousePos_toWindow = pos(0, 0)
        self.mouseButtonDown = False
        center=getattr(values, "CENTER")
        self.isSpeaking = False
        # attribute
        self.item = ""
        self.face = "face_happy"
        self.feet="foot_stand"
        self.status="stand"
        self.pos = pos(center.x, center.y)
        self.isLive = True
        self.taskList:list[task] = []
        self.runTime=0
        self.generator=Generator()
        # init
        self.mainWindow = QMainWindow()
        self.ui = pet.Ui_Form()
        self.ui.setupUi(self.mainWindow)
        self.id = id
        self.ui.pet.setPixmap(
            QtGui.QPixmap(
                f"resources/image/{['icon.png', 'icon1.png', 'icon2.png', 'icon3.png', 'icon4.png', 'icon5.png', 'icon6.png'][num]}"
                # type: ignore
            )
        )  # type: ignore # type: ignore
        self.mainWindow.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.mainWindow.setAttribute(Qt.Qt.WA_TranslucentBackground)

        self.mainWindow.mousePressEvent = self.mousePressEvent  # type: ignore
        self.mainWindow.mouseMoveEvent = self.mouseMoveEvent  # type: ignore
        self.mainWindow.mouseReleaseEvent = self.mouseReleaseEvent  # type: ignore

        self.mainWindow.show()
        self.move(center)
        self.taskList.append(task(self.moveLogic,type="moveLogic",tag="logicCalculator"))
        self.taskList.append(task(self.speakLogic,type="speakLogic",tag="logicCalculator"))
        self.returnSignal.connect(self.speak)
        self.generator.init()
    def speak(self,text):
        logger.info(f"speak {text}")
        self.isSpeaking=False
    def speakLogic(self,_task=None):
        if random.randint(0,1000)>=10 and self.isSpeaking:
            return
        self.isSpeaking=True
        
        nlpSystem.addNLPTask("hello",self.returnSignal,self.generator)
    def moveLogic(self,_task=None):
        a=random.randint(0,1000)
        existingTypes=[]
        for i in self.taskList:
            existingTypes.append(i.infos["tag"])
        if a!=0 and ("playMode"in existingTypes or "stand" in existingTypes):
            return
        # print(bool(self.taskList))
        # print(not self.taskList)
        width:int = getattr(values,'SCREEN_WIDTH')
        height:int = getattr(values,"SCREEN_HEIGHT")
        rect_bottom_left=getattr(values, "RECT_BOTTOM_LEFT")
        rect_bottom_right = getattr(values, "RECT_BOTTOM_RIGHT")
        if self.status == "playMode":
            self.taskList.extend(changeTo_move_step(task(self.moveTaskFunction,
                                      lambda task: task.infos['distance']<=0,
                                      type="move_endpoint",
                                      speed=2,
                                      endpoint=pos(random.randint(0, width), random.randint(0, height)),
                                      tag = "playMode"
                                      ),self))

        elif self.status == "stand":
            if not inRect(self,rect_bottom_left) or inRect(self,rect_bottom_right):
                self.taskList.extend(changeTo_move_step(task(self.moveTaskFunction,
                                      lambda task: task.infos['distance']<=0,
                                      type="move_endpoint",
                                      speed=2,
                                      endpoint=random.choice([
                                        pos(0, height - 50 - 120),
                                        pos(width - 120, height - 50 - 120)
                                        ]),
                                      tag="stand"
                                      ),self))
        

    def awaken(self):
        if self.mouseButtonDown:
            return 
        # if self.runTime%10==5:
            # logger.info("")
            # pprint(self.taskList)
            # print(len(self.taskList))
        executedTypes=[]
        for task in self.taskList:
            if task.infos['type'] in executedTypes:
                continue
            task.run_(task,) # type: ignore
            # logger.debug(task.ifRemove(task,))
            if task.ifRemove(task,):
                self.taskList.remove(task)
                # logger.debug("run del")
                # pprint(self.taskList)
                continue
            executedTypes.append(task.infos["type"])
        # pprint(self.taskList)



        self.runTime+=1
    def moveTaskFunction(self,task:task):
        type=task.infos["type"]
        speed = task.infos["speed"]
        if type == "move_step":
            distance = task.infos["distance"]
            direction = task.infos["direction"]
            if distance>=speed:
                direction_dict = {
                    "north": (0, -speed),
                    "south": (0, speed),
                    "east": (speed, 0),
                    "west": (-speed, 0),
                }
                self.pos.x += direction_dict[direction][0]
                self.pos.y += direction_dict[direction][1]
                distance-=speed
            elif distance <= speed:
                direction_dict = {
                    "north": (0, -distance),
                    "south": (0, distance),
                    "east": (distance, 0),
                    "west": (-distance, 0),
                }
                self.pos.x += direction_dict[direction][0]
                self.pos.y += direction_dict[direction][1]
                distance = 0
            task.infos["distance"] = distance
        self.move(self.pos)

            
    def changeStatus(self, status:str):
        self.status = status
        




    def changeFace(self, face:str):
        if face == "cmd-updata":
            self.ui.face.setPixmap(QtGui.QPixmap(f"resources/image/{self.face}.png"))
            return
        self.face = face
        self.ui.face.setPixmap(QtGui.QPixmap(f"resources/image/{face}.png"))
    def changeFeet(self, feet:str):
        if feet == "cmd-updata":
            self.ui.feet.setPixmap(QtGui.QPixmap(f"resources/image/{self.feet}.png"))
            return
        self.feet = feet
        self.ui.feet.setPixmap(QtGui.QPixmap(f"resources/image/{feet}.png"))
                                                                    
    def changeItem(self, item:str):
        self.item = item
        if item.split(".")[-1] == "png":
            self.ui.item.setPixmap(QtGui.QPixmap(f"resources/image/{item}"))
        elif item.split(".")[-1] != "png":
            self.ui.item.setPixmap(QtGui.QPixmap(f"resources/image/{item}.png"))

    def move(self, pos:pos):
        self.mainWindow.move(int(pos.x), int(pos.y))
        self.pos=pos

    def show(self):
        self.isLive = True
        self.mainWindow.show()

    def hide(self):
        self.isLive = False
        self.mainWindow.hide()

    # override
    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.mouseButtonDown = True
        self.mousePos_toWindow = pos(event.pos().x(), event.pos().y())
        self.changeFace("face___")

    # override
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        curPos = QCursor.pos()
        windowPos = self.mousePos_toWindow
        self.move(pos(curPos.x() - windowPos.x, curPos.y() - windowPos.y))

    # override
    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self.mouseButtonDown = False
        self.mousePos_toWindow = pos(0, 0)
        curPos = QCursor.pos()
        self.pos = pos(
            curPos.x() - self.mousePos_toWindow.x, curPos.y() - self.mousePos_toWindow.y
        )
        self.changeFace("face_happy")
