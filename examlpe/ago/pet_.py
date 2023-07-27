import random
import time
from dataclasses import dataclass

from PyQt5 import QtGui
from PyQt5.QtGui import QMouseEvent, QCursor
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import Qt  # PyQt5 相关

import AI_
import pet
import public


class Pet(object):
    # 使用 dataclass 装饰器来定义一个简单的类，包含 x 和 y 属性
    @dataclass
    class pos:
        """
        主界面坐标信息
        """
        x: float = 0
        y: float = 0

    def __init__(self, main):
        # 初始化当前位置、主界面和一些固定的位置
        self.nowPos = self.pos(int(public.Value.width / 2), int(public.Value.height / 2))  # 当前位置
        self.home = self.pos(0, 0)  # 固定在左上角的位置
        self.center = self.pos(int(public.Value.width / 2), int(public.Value.height / 2))  # 屏幕中心位置
        self.__bottom = self.pos(0, 900)  # 屏幕底部位置
        self.mainWindow = QMainWindow()
        self.ui = pet.Ui_Form()
        self.ui.setupUi(self.mainWindow)

        self.mainWindow.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.mainWindow.setAttribute(Qt.Qt.WA_TranslucentBackground)
        self.ui.pet.setPixmap(QtGui.QPixmap(
            f"resources/image/{['icon.png', 'icon1.png', 'icon2.png', 'icon3.png', 'icon4.png', 'icon5.png', 'icon6.png'][len(main.pets)]}"))
        self.mainWindow.show()
        self.mouseButtonDown = False
        self.id = ["slime", "red", "orange", "yellow", "green", "blue", "purple"][len(main.pets)]
        self.main = main
        self.initAI()
        self.setMouseEvent()

    def mainWindow_re__mousePressEvent(self, event: QMouseEvent = None):
        print("mainWindow_re__mousePressEvent running---", self.id)
        #
        self.mouseButtonDown = True
        self.mousePos_toWindow = self.pos(event.pos().x(), event.pos().y())
        #
        print(self.id, "mouseButtonDown changed:", self.mouseButtonDown, "mousePos_toWindow changed:",
              self.pos(event.pos().x(), event.pos().y()))
        print("\n")

    def mainWindow_re__mouseReleaseEvent(self, event: QMouseEvent = None):
        print("mainWindow_re__mouseReleaseEvent running---", self.id)
        #
        self.mouseButtonDown = False
        self.mousePos_toWindow = self.pos(0, 0)
        pos = QCursor.pos()
        self.nowPos = self.pos(pos.x() - self.mousePos_toWindow.x, pos.y() - self.mousePos_toWindow.y)
        print(self.id, "mouseButtonDown changed:", self.mouseButtonDown)
        print("\n")

    def mainWindow_re__mouseMoveEvent(self, event):
        print("mainWindow_re__mouseMoveEvent running---", self.id)
        #
        self.mouseButtonDown = False
        pos = QCursor.pos()
        window_pos = self.mousePos_toWindow
        print("mouse pos:", (pos.x(), pos.y()), "id:", self.id)
        print("mouse pos window:", (window_pos.x, window_pos.y), "id:", self.id)
        print("mouse pos move to:", (pos.x() - window_pos.x, pos.y() - window_pos.y), "id:", self.id)
        self.moveMainWindow(self.pos(pos.x() - window_pos.x, pos.y() - window_pos.y))

        print(self.id, "mouseButtonDown changed:", self.mouseButtonDown)
        print("\n")

    def setMouseEvent(self):

        print("setMouseEvent running---", self.id)
        self.mousePos_toWindow = self.pos(0, 0)
        self.mainWindow.mousePressEvent = self.mainWindow_re__mousePressEvent
        self.mainWindow.mouseMoveEvent = self.mainWindow_re__mouseMoveEvent
        self.mainWindow.mouseReleaseEvent = self.mainWindow_re__mouseReleaseEvent
        print("\n")

    def moveMainWindow(self, pos):
        print("moveMainWindow running---", self.id, "move to :", pos, "time:", time.time())
        self.mainWindow.move(int(pos.x), int(pos.y))
        print("\n", "time:", time.time())

    def hide(self):
        self.mainWindow.hide()

    def show(self):
        self.mainWindow.show()

    def moveStep(self, direction, distance):
        print("moveStep running---", self.id, "move step:", direction, distance, "time:", time.time())
        match direction:
            case "north":
                for i in range(distance):
                    self.nowPos.y -= 1
                    self.moveMainWindow(self.nowPos)

            case "south":
                for i in range(distance):
                    self.nowPos.y += 1
                    self.moveMainWindow(self.nowPos)

            case "east":
                for i in range(distance):
                    self.nowPos.x += 1
                    self.moveMainWindow(self.nowPos)

            case "west":
                for i in range(distance):
                    self.nowPos.x -= 1
                    self.moveMainWindow(self.nowPos)
        print("\n", "time:", time.time())

    def bottomPosUpdate(self):
        self.__bottom = self.pos(self.nowPos.x, 900)
        return self.__bottom

    def walk(self, actuator):
        self.moveStep(random.choice(["east", 'south', 'north', 'west']), int(random.randint(50, 300)))

    def walk_condition(self, actuator):
        if random.randint(0, 10) == 0:
            return True

    def initAI(self):
        print(f"{self.id} initAI running")
        self.AI = AI_.AI(self.main, self)
        self.AI.add(AI_.Actuators(self.walk, self.walk_condition, self.AI))
        self.main.timerFuncs.append(self.AI.makeDecisions)
