# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Desktop_Pet.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(703, 745)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/image/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setContentsMargins(0, -1, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Box = QtWidgets.QVBoxLayout()
        self.Box.setObjectName("Box")
        self.Pet = QtWidgets.QGroupBox(self.centralwidget)
        self.Pet.setObjectName("Pet")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Pet)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.Pet)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.toolBox = QtWidgets.QToolBox(self.frame)
        self.toolBox.setGeometry(QtCore.QRect(0, 10, 681, 381))
        self.toolBox.setObjectName("toolBox")
        self.Slime = QtWidgets.QWidget()
        self.Slime.setGeometry(QtCore.QRect(0, 0, 681, 136))
        self.Slime.setObjectName("Slime")
        self.frame_2 = QtWidgets.QFrame(self.Slime)
        self.frame_2.setGeometry(QtCore.QRect(130, 0, 120, 80))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pet = QtWidgets.QLabel(self.frame_2)
        self.pet.setGeometry(QtCore.QRect(40, 0, 80, 80))
        self.pet.setText("")
        self.pet.setPixmap(QtGui.QPixmap(":/icon/image/icon.png"))
        self.pet.setScaledContents(True)
        self.pet.setObjectName("pet")
        self.item = QtWidgets.QLabel(self.frame_2)
        self.item.setGeometry(QtCore.QRect(0, 20, 48, 48))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.item.setFont(font)
        self.item.setText("")
        self.item.setPixmap(QtGui.QPixmap(":/image/image/cookie.png"))
        self.item.setScaledContents(True)
        self.item.setObjectName("item")
        self.toolBox.addItem(self.Slime, icon, "")
        self.red = QtWidgets.QWidget()
        self.red.setGeometry(QtCore.QRect(0, 0, 681, 136))
        self.red.setObjectName("red")
        self.frame_3 = QtWidgets.QFrame(self.red)
        self.frame_3.setGeometry(QtCore.QRect(130, 10, 131, 91))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pet_2 = QtWidgets.QLabel(self.frame_3)
        self.pet_2.setGeometry(QtCore.QRect(50, 10, 80, 80))
        self.pet_2.setText("")
        self.pet_2.setPixmap(QtGui.QPixmap(":/icon/image/icon1.png"))
        self.pet_2.setScaledContents(True)
        self.pet_2.setObjectName("pet_2")
        self.item_2 = QtWidgets.QLabel(self.frame_3)
        self.item_2.setGeometry(QtCore.QRect(10, 30, 48, 48))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.item_2.setFont(font)
        self.item_2.setText("")
        self.item_2.setPixmap(QtGui.QPixmap(":/image/image/cookie.png"))
        self.item_2.setScaledContents(True)
        self.item_2.setObjectName("item_2")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.red, icon1, "")
        self.orange = QtWidgets.QWidget()
        self.orange.setGeometry(QtCore.QRect(0, 0, 681, 136))
        self.orange.setObjectName("orange")
        self.frame_4 = QtWidgets.QFrame(self.orange)
        self.frame_4.setGeometry(QtCore.QRect(140, 20, 131, 91))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pet_3 = QtWidgets.QLabel(self.frame_4)
        self.pet_3.setGeometry(QtCore.QRect(50, 10, 80, 80))
        self.pet_3.setText("")
        self.pet_3.setPixmap(QtGui.QPixmap(":/icon/image/icon2.png"))
        self.pet_3.setScaledContents(True)
        self.pet_3.setObjectName("pet_3")
        self.item_3 = QtWidgets.QLabel(self.frame_4)
        self.item_3.setGeometry(QtCore.QRect(10, 30, 48, 48))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.item_3.setFont(font)
        self.item_3.setText("")
        self.item_3.setPixmap(QtGui.QPixmap(":/image/image/cookie.png"))
        self.item_3.setScaledContents(True)
        self.item_3.setObjectName("item_3")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/image/icon2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.orange, icon2, "")
        self.yellow = QtWidgets.QWidget()
        self.yellow.setGeometry(QtCore.QRect(0, 0, 681, 136))
        self.yellow.setObjectName("yellow")
        self.frame_5 = QtWidgets.QFrame(self.yellow)
        self.frame_5.setGeometry(QtCore.QRect(180, 30, 131, 91))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.pet_4 = QtWidgets.QLabel(self.frame_5)
        self.pet_4.setGeometry(QtCore.QRect(50, 10, 80, 80))
        self.pet_4.setText("")
        self.pet_4.setPixmap(QtGui.QPixmap(":/icon/image/icon3.png"))
        self.pet_4.setScaledContents(True)
        self.pet_4.setObjectName("pet_4")
        self.item_4 = QtWidgets.QLabel(self.frame_5)
        self.item_4.setGeometry(QtCore.QRect(10, 30, 48, 48))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.item_4.setFont(font)
        self.item_4.setText("")
        self.item_4.setPixmap(QtGui.QPixmap(":/image/image/cookie.png"))
        self.item_4.setScaledContents(True)
        self.item_4.setObjectName("item_4")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/image/icon3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.yellow, icon3, "")
        self.green = QtWidgets.QWidget()
        self.green.setGeometry(QtCore.QRect(0, 0, 681, 136))
        self.green.setObjectName("green")
        self.frame_6 = QtWidgets.QFrame(self.green)
        self.frame_6.setGeometry(QtCore.QRect(180, 30, 131, 91))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.pet_5 = QtWidgets.QLabel(self.frame_6)
        self.pet_5.setGeometry(QtCore.QRect(50, 10, 80, 80))
        self.pet_5.setText("")
        self.pet_5.setPixmap(QtGui.QPixmap(":/icon/image/icon4.png"))
        self.pet_5.setScaledContents(True)
        self.pet_5.setObjectName("pet_5")
        self.item_5 = QtWidgets.QLabel(self.frame_6)
        self.item_5.setGeometry(QtCore.QRect(10, 30, 48, 48))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.item_5.setFont(font)
        self.item_5.setText("")
        self.item_5.setPixmap(QtGui.QPixmap(":/image/image/cookie.png"))
        self.item_5.setScaledContents(True)
        self.item_5.setObjectName("item_5")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/image/icon4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.green, icon4, "")
        self.blue = QtWidgets.QWidget()
        self.blue.setGeometry(QtCore.QRect(0, 0, 681, 136))
        self.blue.setObjectName("blue")
        self.frame_7 = QtWidgets.QFrame(self.blue)
        self.frame_7.setGeometry(QtCore.QRect(180, 30, 131, 91))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.pet_6 = QtWidgets.QLabel(self.frame_7)
        self.pet_6.setGeometry(QtCore.QRect(50, 10, 80, 80))
        self.pet_6.setText("")
        self.pet_6.setPixmap(QtGui.QPixmap(":/icon/image/icon5.png"))
        self.pet_6.setScaledContents(True)
        self.pet_6.setObjectName("pet_6")
        self.item_6 = QtWidgets.QLabel(self.frame_7)
        self.item_6.setGeometry(QtCore.QRect(10, 30, 48, 48))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.item_6.setFont(font)
        self.item_6.setText("")
        self.item_6.setPixmap(QtGui.QPixmap(":/image/image/cookie.png"))
        self.item_6.setScaledContents(True)
        self.item_6.setObjectName("item_6")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/image/icon5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.blue, icon5, "")
        self.purple = QtWidgets.QWidget()
        self.purple.setGeometry(QtCore.QRect(0, 0, 681, 136))
        self.purple.setObjectName("purple")
        self.frame_8 = QtWidgets.QFrame(self.purple)
        self.frame_8.setGeometry(QtCore.QRect(170, 40, 131, 91))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.pet_7 = QtWidgets.QLabel(self.frame_8)
        self.pet_7.setGeometry(QtCore.QRect(50, 10, 80, 80))
        self.pet_7.setText("")
        self.pet_7.setPixmap(QtGui.QPixmap(":/icon/image/icon6.png"))
        self.pet_7.setScaledContents(True)
        self.pet_7.setObjectName("pet_7")
        self.item_7 = QtWidgets.QLabel(self.frame_8)
        self.item_7.setGeometry(QtCore.QRect(10, 30, 48, 48))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.item_7.setFont(font)
        self.item_7.setText("")
        self.item_7.setPixmap(QtGui.QPixmap(":/image/image/cookie.png"))
        self.item_7.setScaledContents(True)
        self.item_7.setObjectName("item_7")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/image/icon6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.purple, icon6, "")
        self.verticalLayout.addWidget(self.frame)
        self.Box.addWidget(self.Pet)
        self.Ctrl_Panel = QtWidgets.QGroupBox(self.centralwidget)
        self.Ctrl_Panel.setObjectName("Ctrl_Panel")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Ctrl_Panel)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tabs = QtWidgets.QTabWidget(self.Ctrl_Panel)
        self.tabs.setObjectName("tabs")
        self.BiaoQing_zh_2 = QtWidgets.QWidget()
        self.BiaoQing_zh_2.setObjectName("BiaoQing_zh_2")
        self.gridLayout = QtWidgets.QGridLayout(self.BiaoQing_zh_2)
        self.gridLayout.setObjectName("gridLayout")
        self.compass = QtWidgets.QPushButton(self.BiaoQing_zh_2)
        self.compass.setObjectName("compass")
        self.gridLayout.addWidget(self.compass, 0, 2, 1, 1)
        self.bread = QtWidgets.QPushButton(self.BiaoQing_zh_2)
        self.bread.setObjectName("bread")
        self.gridLayout.addWidget(self.bread, 2, 0, 1, 1)
        self.pickaxe = QtWidgets.QPushButton(self.BiaoQing_zh_2)
        self.pickaxe.setObjectName("pickaxe")
        self.gridLayout.addWidget(self.pickaxe, 0, 0, 1, 1)
        self.random = QtWidgets.QPushButton(self.BiaoQing_zh_2)
        self.random.setObjectName("random")
        self.gridLayout.addWidget(self.random, 4, 2, 1, 1)
        self.apple = QtWidgets.QPushButton(self.BiaoQing_zh_2)
        self.apple.setObjectName("apple")
        self.gridLayout.addWidget(self.apple, 2, 2, 1, 1)
        self.tabs.addTab(self.BiaoQing_zh_2, "")
        self.move_en = QtWidgets.QWidget()
        self.move_en.setObjectName("move_en")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.move_en)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.moveToHome_Button = QtWidgets.QPushButton(self.move_en)
        self.moveToHome_Button.setObjectName("moveToHome_Button")
        self.gridLayout_2.addWidget(self.moveToHome_Button, 0, 0, 1, 1)
        self.moveToTheBottomOfTheScreen_button = QtWidgets.QPushButton(self.move_en)
        self.moveToTheBottomOfTheScreen_button.setObjectName("moveToTheBottomOfTheScreen_button")
        self.gridLayout_2.addWidget(self.moveToTheBottomOfTheScreen_button, 1, 0, 1, 1)
        self.moveToRandomPos_button = QtWidgets.QPushButton(self.move_en)
        self.moveToRandomPos_button.setObjectName("moveToRandomPos_button")
        self.gridLayout_2.addWidget(self.moveToRandomPos_button, 1, 1, 1, 1)
        self.moveToTheCenterOfTheScreen_button = QtWidgets.QPushButton(self.move_en)
        self.moveToTheCenterOfTheScreen_button.setObjectName("moveToTheCenterOfTheScreen_button")
        self.gridLayout_2.addWidget(self.moveToTheCenterOfTheScreen_button, 0, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.move_en)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 3, 0, 1, 2)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.south = QtWidgets.QPushButton(self.move_en)
        self.south.setObjectName("south")
        self.gridLayout_4.addWidget(self.south, 0, 1, 1, 1)
        self.east = QtWidgets.QPushButton(self.move_en)
        self.east.setObjectName("east")
        self.gridLayout_4.addWidget(self.east, 0, 0, 1, 1)
        self.north = QtWidgets.QPushButton(self.move_en)
        self.north.setObjectName("north")
        self.gridLayout_4.addWidget(self.north, 1, 0, 1, 1)
        self.west = QtWidgets.QPushButton(self.move_en)
        self.west.setObjectName("west")
        self.gridLayout_4.addWidget(self.west, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 5, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nSteps = QtWidgets.QLineEdit(self.move_en)
        self.nSteps.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.nSteps.setObjectName("nSteps")
        self.horizontalLayout.addWidget(self.nSteps)
        self.gridLayout_2.addLayout(self.horizontalLayout, 4, 0, 1, 2)
        self.tabs.addTab(self.move_en, "")
        self.Settings_en = QtWidgets.QWidget()
        self.Settings_en.setObjectName("Settings_en")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.Settings_en)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.goHome = QtWidgets.QPushButton(self.Settings_en)
        self.goHome.setObjectName("goHome")
        self.gridLayout_5.addWidget(self.goHome, 0, 0, 1, 1)
        self.goOut = QtWidgets.QPushButton(self.Settings_en)
        self.goOut.setObjectName("goOut")
        self.gridLayout_5.addWidget(self.goOut, 1, 0, 1, 1)
        self.frame_9 = QtWidgets.QFrame(self.Settings_en)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.status = QtWidgets.QComboBox(self.frame_9)
        self.status.setObjectName("status")
        self.status.addItem("")
        self.status.addItem("")
        self.status.addItem("")
        self.gridLayout_6.addWidget(self.status, 2, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_9, 2, 0, 1, 1)
        self.tabs.addTab(self.Settings_en, "")
        self.verticalLayout_7.addWidget(self.tabs)
        self.Box.addWidget(self.Ctrl_Panel)
        self.Box.setStretch(0, 2)
        self.Box.setStretch(1, 1)
        self.gridLayout_3.addLayout(self.Box, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 703, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(3)
        self.tabs.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabs, self.pickaxe)
        MainWindow.setTabOrder(self.pickaxe, self.bread)
        MainWindow.setTabOrder(self.bread, self.compass)
        MainWindow.setTabOrder(self.compass, self.apple)
        MainWindow.setTabOrder(self.apple, self.random)
        MainWindow.setTabOrder(self.random, self.moveToHome_Button)
        MainWindow.setTabOrder(self.moveToHome_Button, self.moveToTheCenterOfTheScreen_button)
        MainWindow.setTabOrder(self.moveToTheCenterOfTheScreen_button, self.moveToTheBottomOfTheScreen_button)
        MainWindow.setTabOrder(self.moveToTheBottomOfTheScreen_button, self.moveToRandomPos_button)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DesktopPet"))
        self.Pet.setTitle(_translate("MainWindow", "Pet"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Slime), _translate("MainWindow", "Slime"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.red), _translate("MainWindow", "red"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.orange), _translate("MainWindow", "orange"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.yellow), _translate("MainWindow", "yellow"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.green), _translate("MainWindow", "green"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.blue), _translate("MainWindow", "blue"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.purple), _translate("MainWindow", "purple"))
        self.Ctrl_Panel.setTitle(_translate("MainWindow", "Ctrl Panel"))
        self.compass.setText(_translate("MainWindow", "compass"))
        self.bread.setText(_translate("MainWindow", "bread"))
        self.pickaxe.setText(_translate("MainWindow", "pickaxe"))
        self.random.setText(_translate("MainWindow", "random"))
        self.apple.setText(_translate("MainWindow", "apple"))
        self.tabs.setTabText(self.tabs.indexOf(self.BiaoQing_zh_2), _translate("MainWindow", "物品"))
        self.moveToHome_Button.setText(_translate("MainWindow", "home"))
        self.moveToTheBottomOfTheScreen_button.setText(_translate("MainWindow", "bottom"))
        self.moveToRandomPos_button.setText(_translate("MainWindow", "random"))
        self.moveToTheCenterOfTheScreen_button.setText(_translate("MainWindow", "center"))
        self.south.setText(_translate("MainWindow", "south"))
        self.east.setText(_translate("MainWindow", "east"))
        self.north.setText(_translate("MainWindow", "north"))
        self.west.setText(_translate("MainWindow", "west"))
        self.tabs.setTabText(self.tabs.indexOf(self.move_en), _translate("MainWindow", "移动"))
        self.goHome.setText(_translate("MainWindow", "回家"))
        self.goOut.setText(_translate("MainWindow", "出来溜溜"))
        self.status.setItemText(0, _translate("MainWindow", "原地站立"))
        self.status.setItemText(1, _translate("MainWindow", "工作模式"))
        self.status.setItemText(2, _translate("MainWindow", "玩耍状态"))
        self.tabs.setTabText(self.tabs.indexOf(self.Settings_en), _translate("MainWindow", "设置"))
import test_rc