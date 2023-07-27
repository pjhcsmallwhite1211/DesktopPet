# 导入模块
import os  # 包含操作系统相应的功能
import random  # 生成随机数
import sys  # 提供了对 Python 解释器进行访问和一些与解释器强烈交互的变量和函数
from concurrent.futures import ThreadPoolExecutor  # 支持多线程
from dataclasses import dataclass  # 引入数据类，可以快速创建一个类

from PyQt5 import Qt  # PyQt5 相关
from PyQt5.QtWidgets import QApplication, QMainWindow  # PyQt5 相关组件
from pyqt5_plugins.examplebuttonplugin import QtGui  # 自定义的插件

import AI
from examlpe.ago import Desktop_Pet, block
import pet  # 导入自定义模块

threadPool = ThreadPoolExecutor(max_workers=5)  # 创建5个线程


class BlockList(object):
    class Block(object):
        def __init__(self):
            self.window = None
            self.ui = None
            self.pos = None

        def __repr__(self):
            return f'<Block window={self.window},ui={self.ui},pos={self.pos}>'

    def __init__(self):
        self.blockList = []

    def add(self, block):
        self.blockList.append(block)


class DesktopPet(object):
    """
    桌宠主界面相关的操作
    """

    def __init__(self):
        pass

    def itemButtonClicked(self, item, value):
        """
        切换 item 图片
        """
        value.ui.item.setPixmap(QtGui.QPixmap(f":/image/image/{item}"))  # 切换 item 图片
        value.ui2.item.setPixmap(QtGui.QPixmap(f":/image/image/{item}"))

    def randomItem(self):
        """
        从资源文件夹中随机获取一张图片
        """
        list = []

        # 使用递归遍历资源文件夹，把所有图片存放在列表中
        def forDir(path_):
            for path, childDir, files in os.walk(path_):
                if not childDir:  # 遍历到底层目录
                    list.extend(files)
                else:
                    forDir(path + "/" + childDir[0])  # 沿着子目录递归遍历

        forDir("./resources/image")
        return random.choice(list)  # 随机返回一个图片

    def main1(self, value):
        """
        绑定各个按钮的点击事件
        """
        value.ui.apple.clicked.connect(lambda: self.itemButtonClicked("apple.png", value))
        value.ui.pickaxe.clicked.connect(lambda: self.itemButtonClicked("diamond_pickaxe.png", value))
        value.ui.compass.clicked.connect(lambda: self.itemButtonClicked("compass_18.png", value))
        value.ui.bread.clicked.connect(lambda: self.itemButtonClicked("bread.png", value))
        value.ui.random.clicked.connect(lambda: self.itemButtonClicked(self.randomItem(), value))
        value.ui.moveToHome_Button.clicked.connect(lambda: value.pet.moveMainWindow2(value.pet.home))
        value.ui.moveToRandomPos_button.clicked.connect(lambda: value.pet.moveMainWindow2(
            # 随机移动位置
            value.pet.pos(random.randint(0, int(value.width)), random.randint(0, int(value.height)))))
        # 把主界面移到屏幕底部
        value.ui.moveToTheBottomOfTheScreen_button.clicked.connect(
            lambda: value.pet.moveMainWindow2(value.pet.bottomPosUpdate()))
        # 把主界面移到屏幕中央
        value.ui.moveToTheCenterOfTheScreen_button.clicked.connect(
            lambda: value.pet.moveMainWindow2(value.pet.center))
        value.ui.east.clicked.connect(lambda: value.pet.moveStep("east", int(value.ui.nSteps.text())))
        value.ui.west.clicked.connect(lambda: value.pet.moveStep("west", int(value.ui.nSteps.text())))
        value.ui.north.clicked.connect(lambda: value.pet.moveStep("north", int(value.ui.nSteps.text())))
        value.ui.south.clicked.connect(lambda: value.pet.moveStep("south", int(value.ui.nSteps.text())))
        value.ui.nSteps.setText("200")


class Pet(object):
    """
    桌宠操作类
    """

    # 使用 dataclass 装饰器来定义一个简单的类，包含 x 和 y 属性
    @dataclass
    class pos:
        """
        主界面坐标信息
        """
        x: float = 0
        y: float = 0

    def __init__(self, value):
        # 初始化当前位置、主界面和一些固定的位置
        self.nowPos = self.pos(int(value.width / 2), int(value.height / 2))  # 当前位置
        self.home = self.pos(0, 0)  # 固定在左上角的位置
        self.center = self.pos(int(value.width / 2), int(value.height / 2))  # 屏幕中心位置
        self.__bottom = self.pos(0, 900)  # 屏幕底部位置

    def bottomPosUpdata(self):
        """
        更新底部位置信息
        """
        self.__bottom = self.pos(self.nowPos.x, 900)
        return self.__bottom

    def moveMainWindow2(self, pos, value):
        """
        移动主界面到指定位置
        """
        value.mainWindow2.move(pos.x, pos.y)

    def moveStep(self, forward, distance, value):
        """
        根据方向和距离移动指定的步数
        """
        print('kdosakdpokapokfpospgpanh;sdvmskmdvkk')
        match forward:
            case "north":  # 向北走
                for i in range(distance):
                    self.nowPos.y -= 1
                    value.mainWindow2.move(self.nowPos.x, self.nowPos.y)  # 移动主界面
            case "south":  # 向南走
                for i in range(distance):
                    self.nowPos.y += 1
                    value.mainWindow2.move(self.nowPos.x, self.nowPos.y)
            case "east":  # 向东走
                for i in range(distance):
                    self.nowPos.x += 1
                    value.mainWindow2.move(self.nowPos.x, self.nowPos.y)
            case "west":  # 向西走
                for i in range(distance):
                    self.nowPos.x -= 1
                    value.mainWindow2.move(self.nowPos.x, self.nowPos.y)

    def main2(self, value):
        """
        辅助窗口的风格和样式
        """
        value.mainWindow2.setWindowFlags(Qt.Qt.FramelessWindowHint)  # 设置辅助窗口无边框
        value.mainWindow2.setAttribute(Qt.Qt.WA_TranslucentBackground)  # 设置透明背景


class Task(object):
    def __init__(self, length, funcs):
        self.__len = length
        self.__count = 0
        self.__taskFuncs = funcs

    # 获取 Len 属性的 get 方法
    def getLen(self):
        return self.__len

    # 设置 Len 属性的 set 方法
    def setLen(self, length):
        self.__len = length

    # 获取 Count 属性的 get 方法
    def getCount(self):
        return self.__count

    # 设置 Count 属性的 set 方法
    def setCount(self, count):
        self.__count = count

    # 获取 TaskFuncs 属性的 get 方法

    def setCountUp(self):
        self.__count += 1

    def getTaskFuncs(self):
        return self.__taskFuncs

    # 设置 TaskFuncs 属性的 set 方法
    def setTaskFuncs(self, funcs):
        self.__taskFuncs = funcs

    def run(self, value):
        self.setCountUp()
        self.__taskFuncs[self.getCount()](value)


class MainLoop(object):

    def __init__(self):
        self.__taskList = []
        self.__taskNum = 0

    def addTask(self, Task):
        self.__taskList.append(Task)
        self.__taskNum += 1

    def run(self, value):
        while value.running:
            for task in self.__taskList:
                task.run(value)

    # 获取 TaskList 属性的 get 方法
    def getTaskList(self):
        return self.__taskList

    # 设置 TaskList 属性的 set 方法
    def setTaskList(self, taskList):
        self.__taskList = taskList

    # 获取 TaskNum 属性的 get 方法
    def getTaskNum(self):
        return self.__taskNum

    # 设置 TaskNum 属性的 set 方法
    def setTaskNum(self, taskNum):
        self.__taskNum = taskNum


class Value(object):

    def __init__(self):
        self.app = QApplication(sys.argv)  # 创建 QApplication 实例
        self.running = True

        self.screenRect = self.app.desktop()
        self.screenSize = self.screenRect.size()
        self.width = self.screenSize.width()
        self.height = self.screenSize.height()

        self.mainWindow = QMainWindow()
        self.ui = Desktop_Pet.Ui_MainWindow()  # 使用 PyQt5 Designer 设计的 UI 界面
        self.ui.setupUi(self.mainWindow)
        self.deskTopPet = DesktopPet()
        self.deskTopPet.main1(self)  # 绑定各个按钮的点击事件
        # threadB = threadPool.submit(deskTopPet.main1)
        self.mainWindow.show()

        self.mainWindow2 = QMainWindow()
        self.ui2 = pet.Ui_Form()  # 使用 PyQt5 Designer 设计的 UI 界面
        self.pet = Pet(self)
        self.ui2.setupUi(self.mainWindow2)
        # threadC = threadPool.submit(pet.main2)
        self.pet.main2(self)  # 辅助窗口的风格和样式
        self.mainWindow2.show()

        self.putBlockSignal_ = AI.PutBlockSignal()
        self.putBlockSignal_.putBlocks.connect(self.showWindow)
        self.mainLoop = MainLoop()
        self.threadMainLoop = threadPool.submit(self.mainLoop.run, self)
        self.blockList_ = BlockList()

    def showWindow(self, str, pos):
        block_ = BlockList.Block()
        block_.window = QMainWindow()
        block_.pos = pos
        block_.window.move(block_.pos[0], block_.pos[1])  # 移动主界面
        block_.ui2 = block.Ui_Form()  # 使用 PyQt5 Designer 设计的 UI 界面
        block_.ui2.setupUi(block_.window)
        block_.window.setWindowFlags(Qt.Qt.FramelessWindowHint)  # 设置辅助窗口无边框
        block_.window.setAttribute(Qt.Qt.WA_TranslucentBackground)  # 设置透明背景
        block_.ui2.item.setPixmap(QtGui.QPixmap(f":/image/image/{str}"))
        block_.window.show()
        self.blockList_.add(block_)

    def setValue(self):
        pass


values = Value()

sys.exit(values.app.exec_())
