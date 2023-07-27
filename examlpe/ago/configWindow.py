import os
import random

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow

import Desktop_Pet
import pet_
import public


class ConfigWindow(object):
    def __init__(self,main):
        self.arg = main
        self.mainWindow = QMainWindow()
        self.ui = Desktop_Pet.Ui_MainWindow()
        self.ui.setupUi(self.mainWindow)
        self.createPets()
        self.initUI()
        self.mainWindow.show()
        self.ui.toolBox.currentChanged.connect(self.getNowPet)

    def createPets(self):
        for pet in range(7):
            pet__= pet_.Pet(self.arg)
            pet__.hide()
            self.arg.pets.append(pet__)


    def getNowPet(self):
        self.nowPet: pet_.Pet = self.arg.pets[self.ui.toolBox.currentIndex()]
        return self.nowPet

    def initUI(self):
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
        self.ui.moveToHome_Button.clicked.connect(lambda: self.nowPet.moveMainWindow(self.nowPet.home))  #
        self.ui.moveToRandomPos_button.clicked.connect(lambda: self.nowPet.moveMainWindow(
            # 随机移动位置
            self.nowPet.pos(random.randint(0, int(public.Value.width)), random.randint(0, int(public.Value.height)))))
        # 把主界面移到屏幕底部
        self.ui.moveToTheBottomOfTheScreen_button.clicked.connect(
            lambda: self.nowPet.moveMainWindow(self.nowPet.bottomPosUpdate()))
        # 把主界面移到屏幕中央
        self.ui.moveToTheCenterOfTheScreen_button.clicked.connect(
            lambda: self.nowPet.moveMainWindow(self.nowPet.center))
        self.ui.east.clicked.connect(lambda: self.nowPet.moveStep("east", int(self.ui.nSteps.text())))
        self.ui.west.clicked.connect(lambda: self.nowPet.moveStep("west", int(self.ui.nSteps.text())))
        self.ui.north.clicked.connect(lambda: self.nowPet.moveStep("north", int(self.ui.nSteps.text())))
        self.ui.south.clicked.connect(lambda: self.nowPet.moveStep("south", int(self.ui.nSteps.text())))
        self.ui.nSteps.setText("200")
        self.ui.goHome.clicked.connect(lambda: self.nowPet.hide())
        self.ui.goOut.clicked.connect(lambda: self.nowPet.show())

    def itemButtonClicked(self, item):
        """
        切换 item 图片
        """

        self.ui.item.setPixmap(QtGui.QPixmap(f":/image/image/{item}"))  # 切换 item 图片
        self.nowPet.ui.item.setPixmap(QtGui.QPixmap(f":/image/image/{item}"))

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

        forDir("../../resources/image")
        return random.choice(list)  # 随机返回一个图片
