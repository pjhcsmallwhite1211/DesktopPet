import sys
import time
from concurrent.futures import ThreadPoolExecutor

from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QAction, QSystemTrayIcon, QMenu, QWidget

import public


class Main(QWidget):
    def __init__(self):

        print("dalppppppppppppppppppppppppppppppppppppppppppp")
        self.app = QApplication([])
        QtWidgets.QWidget.__init__(self)
        self.threadPool = ThreadPoolExecutor(max_workers=10)
        self.pets = []
        self.writePublic()

        self.timer = QTimer(self)
        self.timerFuncs=[]
        self.timer.timeout.connect(self.timerFunc)

        self.timer.start(500)

        from configWindow import ConfigWindow
        self.configWindow = ConfigWindow(self)
        self.initMenu()

    def timerFunc(self):
        print("timerFunc running---","time:",time.time())
        for func in self.timerFuncs:
            print("timerFunc cycle running---","time:",time.time())
            func(self)
            print("one cycle done---","time:",time.time())
        print("\n","time:",time.time())
        # pass
    def writePublic(self):

        public.Value.mainType=Main
        public.Value.width = self.app.desktop().size().width()
        public.Value.height = self.app.desktop().size().height()
    def addOnePet(self):
        pass

    def delOnePet(self):
        pass

    def aboutInfo(self):
        pass

    def initMenu(self):
        quit = QAction(QIcon('../../resources/image/icon.png'), "退出", self)
        quit.triggered.connect(self.app.quit)

        addPet = QAction(QIcon('../../resources/image/icon.png'), "添加一个Miku", self)
        addPet.triggered.connect(self.addOnePet)

        removePet = QAction(QIcon('../../resources/image/icon.png'), "移除一个Miku", self)
        removePet.triggered.connect(self.delOnePet)

        about = QAction(QIcon('../../resources/image/icon.png'), "关于", self)
        about.triggered.connect(self.aboutInfo)

        show = QAction(QIcon('../../resources/image/icon.png'), "显示屏幕", self)
        show.triggered.connect(self.configWindow.mainWindow.show)

        hide = QAction(QIcon('../../resources/image/icon.png'), "隐藏屏幕", self)
        hide.triggered.connect(self.configWindow.mainWindow.hide)
        self.trayIconMenu = QMenu(self)  # 创建系统托盘菜单
        self.trayIconMenu.addAction(addPet)  # 将添加宠物操作添加到菜单中
        self.trayIconMenu.addAction(removePet)  # 将移除宠物操作添加到菜单中
        self.trayIconMenu.addAction(about)  # 将关于信息操作添加到菜单中
        self.trayIconMenu.addAction(quit)  # 将退出操作添加到菜单中
        self.trayIconMenu.addAction(show)  # 将显示屏幕操作添加到菜单中
        self.trayIconMenu.addAction(hide)  # 将隐藏屏幕操作添加到菜单中)
        self.trayIcon = QSystemTrayIcon(self)  # 创建系统托盘图标实例
        self.trayIcon.setIcon(QIcon("../../resources/image/icon.png"))  # 设置托盘图标
        self.trayIcon.setContextMenu(self.trayIconMenu)  # 设置托盘图标菜单
        self.trayIcon.show()  # 显示系统托盘图标


if __name__ == '__main__':
    main = Main()


    def getMain():
        return main



    sys.exit(main.app.exec_())
