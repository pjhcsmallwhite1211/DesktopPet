# pyqt的控制窗口
import os
import random

from PyQt5.QtWidgets import QMainWindow
from loguru import logger

import Desktop_Pet
import signalBin


class CtrlWindow(object):
    def __init__(self):
        self.mainWindow = QMainWindow()
        self.ui = Desktop_Pet.Ui_MainWindow()
        self.ui.setupUi(self.mainWindow)
        self.mainWindow.show()

        self.main = None
        signalBin.signalBin.getMain.emit(self)
        logger.info(self.main)
        self.ui.toolBox.currentChanged.connect(self.getNowPet)

        self.initEvents()

    def getNowPet(self):
        self.nowPet = self.main.pets[self.ui.toolBox.currentIndex()]
        return self.nowPet

    def initEvents(self):
        logger.info("init Events")
        self.getNowPet()

        width = self.main.app.desktop().size().width()
        height = self.main.app.desktop().size().height()
        self.ui.apple.clicked.connect(lambda: self.nowPet.changeItem("apple.png"))  #
        self.ui.pickaxe.clicked.connect(lambda: self.nowPet.changeItem("diamond_pickaxe.png"))  #
        self.ui.compass.clicked.connect(lambda: self.nowPet.changeItem("compass_18.png"))  #
        self.ui.bread.clicked.connect(lambda: self.nowPet.changeItem("bread.png"))  #
        self.ui.random.clicked.connect(lambda: self.nowPet.changeItem(self.randomItem()))  #
        self.ui.moveToHome_Button.clicked.connect(lambda: self.nowPet.moveMainWindow(self.nowPet.home))  #
        self.ui.moveToRandomPos_button.clicked.connect(lambda: self.nowPet.moveMainWindow(
            # 随机移动位置
            self.nowPet.pos(random.randint(0, int(width)), random.randint(0, int(height)))))
        # 把主界面移到屏幕底部
        self.ui.moveToTheBottomOfTheScreen_button.clicked.connect(
            lambda: self.nowPet.moveMainWindow(self.nowPet.bottomPosUpdate()))
        # 把主界面移到屏幕中央
        self.ui.moveToTheCenterOfTheScreen_button.clicked.connect(
            lambda: self.nowPet.moveMainWindow(self.nowPet.center))
        self.ui.east.clicked.connect(lambda: self.nowPet.moveStep("east", int(self.ui.nSteps.text()),'m1'))
        self.ui.west.clicked.connect(lambda: self.nowPet.moveStep("west", int(self.ui.nSteps.text()),'m2'))
        self.ui.north.clicked.connect(lambda: self.nowPet.moveStep("north", int(self.ui.nSteps.text()),'m3'))
        self.ui.south.clicked.connect(lambda: self.nowPet.moveStep("south", int(self.ui.nSteps.text()),'m4'))
        self.ui.nSteps.setText("200")
        self.ui.goHome.clicked.connect(lambda: self.nowPet.hide())
        self.ui.goOut.clicked.connect(lambda: self.nowPet.show())
        self.ui.status.activated.connect(lambda: self.nowPet.changeStatus(
            {"原地站立": "stand", "工作模式": "workingMode", "玩耍状态": "playMode","站着":"stop"}[self.ui.status.currentText()]))

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

        forDir("../../resources/image")
        return random.choice(list)  # 随机返回一个图片
