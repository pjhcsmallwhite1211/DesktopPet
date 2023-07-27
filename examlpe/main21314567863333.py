import os
import random
import sys
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QAction, QMenu, QSystemTrayIcon, QMainWindow
from PyQt5 import Qt  # PyQt5 相关

import AI
from examlpe.ago import Desktop_Pet, block
import pet


# 定义Value类，用于存储屏幕的大小信息
class Value(object):
    """
    用于存储屏幕的大小信息
    """
    # 获取屏幕大小
    app = QApplication([])
    screenRect = app.desktop()
    screenSize = screenRect.size()
    width = screenSize.width()
    height = screenSize.height()


# 定义Main类，用于添加一个宠物
class Main(QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        # 创建7个宠物
        for index in range(7):
            self.addOnePet()
            # 隐藏宠物的主窗口
            pets[index].pet.mainWindow.hide()

        # 创建一个DesktopPet实例
        self.desktopPet = DesktopPet()
        # 创建一个退出操作
        quit = QAction("退出", self, triggered=Value.app.quit)  # 创建退出操作
        quit.setIcon(QIcon("img/icon.png"))
        # 创建一个添加一个Miku操作
        addPet = QAction("添加一个Miku", self, triggered=self.addOnePet)  # 创建添加宠物操作
        addPet.setIcon(QIcon("img/icon.png"))
        # 创建一个移除一个Miku操作
        removePet = QAction("移除一个Miku", self, triggered=self.delOnePet)  # 创建移除宠物操作
        removePet.setIcon(QIcon("img/icon.png"))
        # 创建一个关于信息操作
        about = QAction("About", self, triggered=self.aboutInfo)  # 创建关于信息操作
        about.setIcon(QIcon("img/icon.png"))
        # 创建一个显示屏幕操作
        show = QAction("显示屏幕", self, toggled=self.desktopPet.mainWindow.show)  # 创建显示屏幕操作")
        show.setIcon(QIcon("img/icon.png"))
        # 创建一个隐藏屏幕操作
        hide = QAction("隐藏屏幕", self, toggled=self.desktopPet.mainWindow.hide)  # 创建隐藏屏幕操作")
        hide.setIcon(QIcon("img/icon.png"))
        # 创建一个系统托盘菜单
        self.trayIconMenu = QMenu(self)  # 创建系统托盘菜单
        self.trayIconMenu.addAction(addPet)  # 将添加宠物操作添加到菜单中
        self.trayIconMenu.addAction(removePet)  # 将移除宠物操作添加到菜单中
        self.trayIconMenu.addAction(about)  # 将关于信息操作添加到菜单中
        self.trayIconMenu.addAction(quit)  # 将退出操作添加到菜单中
        self.trayIcon = QSystemTrayIcon(self)  # 创建系统托盘图标实例
        self.trayIcon.setIcon(QIcon("resources/image/icon.png"))  # 设置托盘图标
        self.trayIcon.setContextMenu(self.trayIconMenu)  # 设置托盘图标菜单
        self.trayIcon.show()  # 显示系统托盘图标
        for pet in pets:
            pet.pet.initAI(self, blockList_)
            pet.pet.hide_()

    def addOnePet(self):
        global pets
        pets.append(Pet__())

    def delOnePet(self):
        pass

    def aboutInfo(self):
        pass


class DesktopPet(object):
    """
    桌宠主界面相关的操作
    """

    def __init__(self):
        self.mainWindow = QMainWindow()
        self.ui = Desktop_Pet.Ui_MainWindow()  # 使用 PyQt5 Designer 设计的 UI 界面
        self.ui.setupUi(self.mainWindow)
        self.main1()  # 绑定各个按钮的点击事件
        # threadB = threadPool.submit(deskTopPet.main1)
        self.mainWindow.show()
        self.ui.toolBox.currentChanged.connect(self.main1)
        self.getNowPet()

    def getNowPet(self):
        self.pet = pets[self.ui.toolBox.currentIndex()].pet

    def itemButtonClicked(self, item):
        """
        切换 item 图片
        """

        self.ui.item.setPixmap(QtGui.QPixmap(f":/image/image/{item}"))  # 切换 item 图片
        self.pet.ui.item.setPixmap(QtGui.QPixmap(f":/image/image/{item}"))

    def randomItem(self):  #
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

    def main1(self):
        """
        绑定各个按钮的点击事件
        """
        print("init")
        self.getNowPet()
        self.ui.apple.clicked.connect(lambda: self.itemButtonClicked("apple.png"))  #
        self.ui.pickaxe.clicked.connect(lambda: self.itemButtonClicked("diamond_pickaxe.png"))  #
        self.ui.compass.clicked.connect(lambda: self.itemButtonClicked("compass_18.png"))  #
        self.ui.bread.clicked.connect(lambda: self.itemButtonClicked("bread.png"))  #
        self.ui.random.clicked.connect(lambda: self.itemButtonClicked(self.randomItem()))  #
        self.ui.moveToHome_Button.clicked.connect(lambda: self.pet.moveMainWindow2(self.pet.home))  #
        self.ui.moveToRandomPos_button.clicked.connect(lambda: self.pet.moveMainWindow2(
            # 随机移动位置
            self.pet.pos(random.randint(0, int(Value.width)), random.randint(0, int(Value.height)))))
        # 把主界面移到屏幕底部
        self.ui.moveToTheBottomOfTheScreen_button.clicked.connect(
            lambda: self.pet.moveMainWindow2(self.pet.bottomPosUpdate()))
        # 把主界面移到屏幕中央
        self.ui.moveToTheCenterOfTheScreen_button.clicked.connect(lambda: self.pet.moveMainWindow2(self.pet.center))
        self.ui.east.clicked.connect(lambda: self.pet.moveStep("east", int(self.ui.nSteps.text())))
        self.ui.west.clicked.connect(lambda: self.pet.moveStep("west", int(self.ui.nSteps.text())))
        self.ui.north.clicked.connect(lambda: self.pet.moveStep("north", int(self.ui.nSteps.text())))
        self.ui.south.clicked.connect(lambda: self.pet.moveStep("south", int(self.ui.nSteps.text())))
        self.ui.nSteps.setText("200")
        self.ui.goHome.clicked.connect(lambda: self.pet.hide_())
        self.ui.goOut.clicked.connect(lambda: self.pet.show_())


class Pet__(QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.pet = Pet()  # 创建宠物窗口实例


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

    def __init__(self):
        # 初始化当前位置、主界面和一些固定的位置
        self.nowPos = self.pos(int(Value.width / 2), int(Value.height / 2))  # 当前位置
        self.home = self.pos(0, 0)  # 固定在左上角的位置
        self.center = self.pos(int(Value.width / 2), int(Value.height / 2))  # 屏幕中心位置
        self.__bottom = self.pos(0, 900)  # 屏幕底部位置
        self.mainWindow = QMainWindow()
        self.ui = pet.Ui_Form()  # 使用 PyQt5 Designer 设计的 UI 界面
        self.ui.setupUi(self.mainWindow)
        self.main2()
        self.moveMainWindow2(self.bottomPosUpdata())

        self.mainWindow.show()
        self.ui.pet.setPixmap(QtGui.QPixmap(
            f"resources/image/{['icon.png', 'icon1.png', 'icon2.png', 'icon3.png', 'icon4.png', 'icon5.png', 'icon6.png'][len(pets)]}"))  # 设置游戏世界item图片)
        print(
            f"resources/image/{['icon.png', 'icon1.png', 'icon2.png', 'icon3.png', 'icon4.png', 'icon5.png', 'icon6.png'][len(pets)]}")

    def initAI(self, main, blockList_):
        """
        AI 初始化
        :return:
        """
        self.AI = AI.AI({"arg": main.desktopPet})
        self.AI.putBlocks.connect(blockList_.showWindow)
        self.threadA = threadPool.submit(self.AI.run, )

    def hide_(self):
        self.mainWindow.hide()
        self.AI.running = False
        print(self.AI.running)

    def show_(self):
        self.mainWindow.show()
        self.AI.running = True
        print(self.AI.running)

    def bottomPosUpdata(self):
        """
        更新底部位置信息
        """
        self.__bottom = self.pos(self.nowPos.x, 900)
        return self.__bottom

    def moveMainWindow2(self, pos):
        """
        移动主界面到指定位置
        """
        self.mainWindow.move(pos.x, pos.y)

    def moveStep(self, forward, distance):
        """
        根据方向和距离移动指定的步数
        """
        print('kdosakdpokapokfpospgpanh;sdvmskmdvkk')
        match forward:
            case "north":  # 向北走
                for i in range(distance):
                    self.nowPos.y -= 1
                    self.mainWindow.move(int(self.nowPos.x), int(self.nowPos.y))  # 移动主界面
            case "south":  # 向南走
                for i in range(distance):
                    self.nowPos.y += 1
                    self.mainWindow.move(int(self.nowPos.x), int(self.nowPos.y))
            case "east":  # 向东走
                for i in range(distance):
                    self.nowPos.x += 1
                    self.mainWindow.move(int(self.nowPos.x), int(self.nowPos.y))
            case "west":  # 向西走
                for i in range(distance):
                    self.nowPos.x -= 1
                    self.mainWindow.move(int(self.nowPos.x), int(self.nowPos.y))

    def main2(self):
        """
        辅助窗口的风格和样式
        """
        self.mainWindow.setWindowFlags(Qt.Qt.FramelessWindowHint)  # 设置辅助窗口无边框
        self.mainWindow.setAttribute(Qt.Qt.WA_TranslucentBackground)  # 设置透明背景


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
        self.add(block_)


if __name__ == '__main__':
    global pets, blockList_
    pets = []
    blockList_ = BlockList()
    threadPool = ThreadPoolExecutor(max_workers=5)  # 创建5个线程

    main = Main()
    sys.exit(Value.app.exec_())
