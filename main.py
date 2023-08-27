from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QAction, QSystemTrayIcon, QMenu, QWidget
import sys
from controlPanel import controlPanel
from libs import *
app=QApplication(sys.argv)
class Program(QWidget):
    def __init__(self):
        super().__init__()
        width = app.desktop().size().width()
        height = app.desktop().size().height()
        center = pos(int(width / 2), int(height / 2))  # 屏幕中心位置
        home = pos(0, 0)  # 固定在左上角的位置
        bottom_left = pos(0, height)
        bottom_right = pos(width, height)
        top_left = pos(0, 0)
        top_right = pos(width, 0)
        rect_bottom_left = rect(
            bottom_left.x,
            bottom_left.y - 180,
            bottom_left.x + 180,
            bottom_left.y,
        )
        rect_bottom_right = rect(
            bottom_right.x - 180,
            bottom_right.y - 180,
            bottom_right.x,
            bottom_right.y,
        )
        rect_top_left = rect(
            top_left.x,
            top_left.y,
            top_left.x + 180,
            top_left.y + 180,
        )
        rect_top_right = rect(
            top_right.x - 180,
            top_right.y,
            top_right.x,
            top_right.y + 180,
        )
        all = rect(0, 0, width, height)
        images = []
        forDir("./resources/image",images)

        setattr(values,"SCREEN_WIDTH",width)
        setattr(values,"SCREEN_HEIGHT",height)

        setattr(values,"CENTER",center)
        setattr(values,"HOME",home)
        setattr(values,"BOTTOM_LEFT",bottom_left)
        setattr(values,"BOTTOM_RIGHT",bottom_right)
        setattr(values,"TOP_LEFT",top_left)
        setattr(values,"TOP_RIGHT",top_right)

        setattr(values,"RECT_BOTTOM_LEFT",rect_bottom_left)
        setattr(values,"RECT_BOTTOM_RIGHT",rect_bottom_right)
        
        setattr(values,"RECT_TOP_LEFT",rect_top_left)
        setattr(values,"RECT_TOP_RIGHT",rect_top_right)
        setattr(values,"ALL",all)
        setattr(values,"IMAGES",images)
        self.initCtrlPanel()
        self.initMenu()

        
    def initCtrlPanel(self):
        self.controlPanel=controlPanel()
    def initMenu(self):        
        quit = QAction(QIcon('./resources/image/icon.png'), "退出", self)
        quit.triggered.connect(app.quit)

        about = QAction(QIcon('./resources/image/icon.png'), "关于", self)
        about.triggered.connect(lambda :print("info"))

        show = QAction(QIcon('./resources/image/icon.png'), "显示屏幕", self)
        show.triggered.connect(lambda :self.controlPanel.system.show(-1))

        hide = QAction(QIcon('./resources/image/icon.png'), "隐藏屏幕", self)
        hide.triggered.connect(lambda :self.controlPanel.system.hide(-1))
        showCtrl = QAction(QIcon('./resources/image/icon.png'), "显示 controlPanel", self)
        showCtrl.triggered.connect(lambda :self.controlPanel.show())

        hideCtrl = QAction(QIcon('./resources/image/icon.png'), "隐藏 controlPanel", self)
        hideCtrl.triggered.connect(lambda :self.controlPanel.hide())
        self.trayIconMenu = QMenu(self)  # 创建系统托盘菜单
        self.trayIconMenu.addAction(about)  # 将关于信息操作添加到菜单中
        self.trayIconMenu.addSeparator()  # 添加分割线
        self.trayIconMenu.addAction(show)  # 将显示屏幕操作添加到菜单中
        self.trayIconMenu.addAction(hide)  # 将隐藏屏幕操作添加到菜单中)
        self.trayIconMenu.addSeparator()  # 添加分割线
        self.trayIconMenu.addAction(showCtrl)
        self.trayIconMenu.addAction(hideCtrl)  
        self.trayIconMenu.addSeparator()  # 添加分割线
        self.trayIconMenu.addAction(quit)  # 将退出操作添加到菜单中

        self.trayIcon = QSystemTrayIcon(self)  # 创建系统托盘图标实例
        self.trayIcon.setIcon(QIcon("./resources/image/icon.png"))  # 设置托盘图标
        self.trayIcon.setContextMenu(self.trayIconMenu)  # 设置托盘图标菜单
        self.trayIcon.show()  # 显示系统托盘图标
if __name__ == '__main__':
    program=Program()
    sys.exit(app.exec_())