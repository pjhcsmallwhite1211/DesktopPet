# 一个pyqt程序
import sys
from concurrent.futures import ThreadPoolExecutor

from PyQt5.QtCore import QObject, QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QAction, QSystemTrayIcon, QMenu, QWidget
from PyQt5 import QtWidgets

import AI
import ctrlWindow
import petC
import signalBin
from loguru import logger

logger.add("./log/out{time}.log", backtrace=True, diagnose=True)


class Main(QWidget):
    class Func(object):
        def __init__(self, func, parent):
            self.func = func
            self.parent = parent

    def __init__(self):
        logger.info("all init start")
        self.app = QApplication(sys.argv)
        QtWidgets.QWidget.__init__(self)
        self.threadPool = ThreadPoolExecutor(max_workers=10)

        self.pets = []
        self.setGetSignal()
        self.initTimer()
        self.initPets()
        self.initCtrlWindow()
        self.initSysMenu()
        self.initGenerator()

    def initGenerator(self):
        self.isGeneratorOK=False
        self.generator = AI.generator(self)
        self.threadInitGenerator=self.threadPool.submit(self.generator.init)
        logger.warning("generator \033[96minited\033[0m~~~~~~~~~~~~~~~~~~~~~")

    def initTimer(self):
        self.timer = QTimer(self)
        self.timerFuncs = []
        self.timer.timeout.connect(self.runTimer)

        self.timer.start(200)

    def runTimer(self):
        # logger.info(f"running,timerFuncs:{self.timerFuncs}")
        for func in self.timerFuncs:
            # logger.info(f"进入方法循环,{self.timerFuncs}")
            if func.parent.active:
                # logger.info("func run")
                func.func()

    def aboutInfo(self):
        pass

    def initCtrlWindow(self):
        logger.info(f"init CtrlWindow")
        self.ctrlWindow = ctrlWindow.CtrlWindow()

    def initPets(self):
        for pet_ in range(7):
            pet__ = petC.Pet()
            pet__.hide()
            self.pets.append(pet__)

    def initSysMenu(self):
        logger.info(f"initSysMenu")
        quit = QAction(QIcon('./resources/image/icon.png'), "退出", self)
        quit.triggered.connect(self.app.quit)

        about = QAction(QIcon('./resources/image/icon.png'), "关于", self)
        about.triggered.connect(self.aboutInfo)

        show = QAction(QIcon('./resources/image/icon.png'), "显示屏幕", self)
        show.triggered.connect(self.ctrlWindow.mainWindow.show)

        hide = QAction(QIcon('./resources/image/icon.png'), "隐藏屏幕", self)
        hide.triggered.connect(self.ctrlWindow.mainWindow.hide)
        self.trayIconMenu = QMenu(self)  # 创建系统托盘菜单
        self.trayIconMenu.addAction(about)  # 将关于信息操作添加到菜单中
        self.trayIconMenu.addAction(quit)  # 将退出操作添加到菜单中
        self.trayIconMenu.addAction(show)  # 将显示屏幕操作添加到菜单中
        self.trayIconMenu.addAction(hide)  # 将隐藏屏幕操作添加到菜单中)
        self.trayIcon = QSystemTrayIcon(self)  # 创建系统托盘图标实例
        self.trayIcon.setIcon(QIcon("./resources/image/icon.png"))  # 设置托盘图标
        self.trayIcon.setContextMenu(self.trayIconMenu)  # 设置托盘图标菜单
        self.trayIcon.show()  # 显示系统托盘图标

    def get(self, obj):
        obj.main = self

    def showValues(self):
        return

    def setGetSignal(self):
        signalBin.signalBin.getMain.connect(self.get)
        signalBin.signalBin.getValues.connect(self.showValues)


if __name__ == '__main__':
    main = Main()

    sys.exit(main.app.exec_())
