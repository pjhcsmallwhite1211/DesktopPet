import random
import threading
import time
from dataclasses import dataclass

from PyQt5.QtGui import QCursor, QMouseEvent
from PyQt5.QtWidgets import QMainWindow
from loguru import logger
from PyQt5 import Qt, QtGui  # PyQt5 相关

import pet
import signalBin
import AI


class Pet(object):
    # 使用 dataclass 装饰器来定义一个简单的类，包含 x 和 y 属性
    @dataclass
    class pos:
        """
        主界面坐标信息
        """
        x: float = 0
        y: float = 0

    @dataclass
    class rect:
        left_top_x: float
        left_top_y: float
        right_bottom_x: float
        right_bottom_y: float

    def __init__(self):
        self.mainWindow = QMainWindow()
        self.ui = pet.Ui_Form()
        self.ui.setupUi(self.mainWindow)
        self.main = None
        signalBin.signalBin.getMain.emit(self)
        self.id = ["slime", "red", "orange", "yellow", "green", "blue", "purple"][len(self.main.pets)]
        self.width = self.main.app.desktop().size().width()
        self.height = self.main.app.desktop().size().height()
        self.nowPos = self.pos(int(self.width / 2), int(self.height / 2))  # 当前位置
        self.home = self.pos(0, 0)  # 固定在左上角的位置
        self.center = self.pos(int(self.width / 2), int(self.height / 2))  # 屏幕中心位置
        self.__bottom = self.pos(0, self.height - 120)  # 屏幕底部位置

        self.mainWindow.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.mainWindow.setAttribute(Qt.Qt.WA_TranslucentBackground)
        self.ui.pet.setPixmap(QtGui.QPixmap(
            f"resources/image/{['icon.png', 'icon1.png', 'icon2.png', 'icon3.png', 'icon4.png', 'icon5.png', 'icon6.png'][len(self.main.pets)]}"))
        self.face = "face_happy"
        self.feet = "foot_stand"
        self.mainWindow.show()
        self.setMouseEvent()
        self.active = True
        self.speed = 5
        self.initAI()
        self.now_status = "stand"

        # 创建屏幕角落的坐标
        self.bottom_left = self.pos(0, self.height)
        self.bottom_right = self.pos(self.width, self.height)
        self.top_left = self.pos(0, 0)
        self.top_right = self.pos(self.width, 0)
        # 生成rect
        self.rect_bottom_left = self.rect(self.bottom_left.x, self.bottom_left.y - 180, self.bottom_left.x + 180,
                                          self.bottom_left.y)
        self.rect_bottom_right = self.rect(self.bottom_right.x - 180, self.bottom_right.y - 180, self.bottom_right.x,
                                           self.bottom_right.y)
        self.rect_top_left = self.rect(self.top_left.x, self.top_left.y, self.top_left.x + 180, self.top_left.y + 180)
        self.rect_top_right = self.rect(self.top_right.x - 180, self.top_right.y, self.top_right.x,
                                        self.top_right.y + 180)
        self.all = self.rect(0, 0, self.width, self.height)

    def changeStatus(self, status):
        self.now_status = status

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

    def mainWindow_re__mousePressEvent(self, event: QMouseEvent = None):
        logger.info(f"mainWindow_re__mousePressEvent running--- {self.id}")
        #
        self.mouseButtonDown = True
        self.mousePos_toWindow = self.pos(event.pos().x(), event.pos().y())
        self.setFace("face___")
        #
        logger.info(
            f"{self.id} mouseButtonDown changed: {self.mouseButtonDown}, mousePos_toWindow changed: {self.pos(event.pos().x(), event.pos().y())}\n")

    def mainWindow_re__mouseReleaseEvent(self, event: QMouseEvent = None):
        logger.info(f"mainWindow_re__mouseReleaseEvent running--- {self.id}")
        #
        self.mouseButtonDown = False
        self.mousePos_toWindow = self.pos(0, 0)
        pos = QCursor.pos()
        self.nowPos = self.pos(pos.x() - self.mousePos_toWindow.x, pos.y() - self.mousePos_toWindow.y)
        self.setFace("face_happy")

        logger.info(f"{self.id} mouseButtonDown changed: {self.mouseButtonDown}\n")

    def mainWindow_re__mouseMoveEvent(self, event):
        logger.info(f"mainWindow_re__mouseMoveEvent running--- {self.id}")
        #
        self.mouseButtonDown = False
        pos = QCursor.pos()
        window_pos = self.mousePos_toWindow
        logger.info(f"mouse pos: ({pos.x()}, {pos.y()}) id: {self.id}")
        logger.info(f"mouse pos window: ({window_pos.x}, {window_pos.y}) id: {self.id}")
        logger.info(f"mouse pos move to: ({pos.x() - window_pos.x}, {pos.y() - window_pos.y}) id: {self.id}")
        self.moveMainWindow(self.pos(pos.x() - window_pos.x, pos.y() - window_pos.y))

        logger.info(f"{self.id} mouseButtonDown changed: {self.mouseButtonDown}\n")

    def setMouseEvent(self):
        logger.info(f"setMouseEvent running--- {self.id}")
        self.mousePos_toWindow = self.pos(0, 0)
        self.mainWindow.mousePressEvent = self.mainWindow_re__mousePressEvent
        self.mainWindow.mouseMoveEvent = self.mainWindow_re__mouseMoveEvent
        self.mainWindow.mouseReleaseEvent = self.mainWindow_re__mouseReleaseEvent
        logger.info("\n")

    def hide(self):
        logger.info(f"{self.id} hide")
        self.mainWindow.hide()
        self.active = False

    def show(self):
        logger.info(f"{self.id} show")
        self.mainWindow.show()
        self.active = True

    def moveMainWindow(self, pos):
        # logger.info(f"moveMainWindow running --- {self.id}, move to: {pos}, time: {time.time()}")
        self.mainWindow.move(int(pos.x), int(pos.y))
        self.nowPos = self.pos(pos.x, pos.y)
        # logger.info(f"\n time: {time.time()}")

    def walkFlash(self, var):
        if var % 5 == 0:
            self.setFeet("foot_right")
            self.ui.feet.repaint()
        elif var % 5 == 3:
            self.setFeet("foot_left")
            self.ui.feet.repaint()

    def moveStep(self, direction, distance, command):
        # logger.info(
        #     f"""moveStep running --- {self.id}:
        #             direction: {direction},
        #             distance: {distance}
        #             cycle:{self.speed * distance},
        #             Δ_plus:{1 / self.speed},
        #             time: {time.time()},
        #             speed:  {self.speed},
        #             nowPos: {self.nowPos},
        #             height: {self.height},
        #             width: {self.width},
        #             status: {self.now_status},
        #             command: {command}
        #
        #
        #     """)
        aStep = 0

        direction_dict = {
            "north": (0, -1 / self.speed),
            "south": (0, 1 / self.speed),
            "east": (1 / self.speed, 0),
            "west": (-1 / self.speed, 0)
        }
        for i in range(int(self.speed * distance)):
            self.nowPos.x += direction_dict[direction][0]
            self.nowPos.y += direction_dict[direction][1]
            self.nowPos.x = round(self.nowPos.x, 1)
            self.nowPos.y = round(self.nowPos.y, 1)

            aStep += 1
            # time.sleep(0.000001)
            self.moveMainWindow(self.nowPos)
            self.walkFlash(aStep)
        # logger.info(
        #     f"aStep:{aStep},move:{(direction_dict[direction][0] * aStep, direction_dict[direction][1] * aStep)},change:{aStep // 5}")

        if not self.inRect(self.all):
            logger.error("move out")
            logger.error(f"nowPos:{self.nowPos},Δx:{1920 - self.nowPos.x},Δy:{self.nowPos.y}")
            raise Exception(f"Out of range")

    def bottomPosUpdate(self):
        self.__bottom = self.pos(self.nowPos.x, self.height - 120)
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
        if rect.left_top_x <= self.nowPos.x <= rect.right_bottom_x and rect.left_top_y <= self.nowPos.y <= rect.right_bottom_y:
            return True

    def walk(self, actuator):
        logger.info(f'{self.id} walking')
        if self.now_status == "playMode":
            logger.debug(f"playing mode,{self.now_status}")
            self.moveStep(random.choice(["east", 'south', 'north', 'west']), int(random.randint(700, 800)), 'p1')
        elif self.now_status == "stand":
            logger.debug(f"standing still,{self.now_status}")
            if not self.inRect(self.rect_bottom_left) or self.inRect(self.rect_bottom_right):
                self.moveStep("south", (self.height - 120) - self.nowPos.y, 's1')
                self.moveStep("west", self.nowPos.x, 's2')
        elif self.now_status == "workingMode":
            logger.debug(f"working mode,{self.now_status}")
            if self.inRect(self.rect_bottom_left):
                direction = random.choice(["east", "north"])
                self.moveStep(direction, random.randint({"north": 600, "east": 700}[direction],
                                                        {"north": self.height, "east": self.width}[direction]), 'w1')
            elif self.inRect(self.rect_bottom_right):
                direction = random.choice(["west", "north"])
                self.moveStep(direction, random.randint({"north": 600, "west": 700}[direction],
                                                        {"north": self.height, "west": self.width}[direction]), 'w2')
            elif self.inRect(self.rect_top_left) or self.inRect(self.rect_top_right):
                self.moveStep("south", random.randint(int((self.height - self.nowPos.y) - 100 - 121),
                                                      int((self.height - self.nowPos.y) - 121)), 'w3')
            else:
                self.moveStep("south", (self.height - 120) - self.nowPos.y, 'w4')
                self.moveStep("west", self.nowPos.x, 'w5')

    #
    # @dataclass
    # class rect:
    #     left_top_x: float
    #     left_top_y: float
    #     left_bottom_x: float
    #     left_bottom_y: float
    #     right_bottom_x: float
    #     right_bottom_y: float
    #     right_top_x: float
    #     right_top_y: float
    def walk_condition(self, actuator):
        if random.randint(0, 10) == 0:
            return True

    def speak_condition(self, actuator):
        if random.randint(0, 10) == 0:
            return True

    def speak(self, actuator):
        logger.info(f"{self.id} speaking")
        threadSpeak = self.main.threadPool.submit(self.main.generator.generateText,"hello")


    def initAI(self):
        logger.info(f"{self.id} initAI running")
        self.AI = AI.AI(self)
        self.AI.add(AI.Actuators(self.walk, self.walk_condition, self.AI))
        self.AI.add(AI.Actuators(self.speak, self.speak_condition, self.AI))
        self.main.timerFuncs.append(self.main.Func(self.AI.makeDecisions, self))
