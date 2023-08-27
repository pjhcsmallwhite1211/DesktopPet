# 一个pyqt程序
import sys
import time
from pprint import pprint

import pysnooper
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QAction, QSystemTrayIcon, QMenu, QWidget
from loguru import logger

import ctrlWindow
import petC
import signalBin

logger.add("./log/out{time}.log", backtrace=True, diagnose=True)


#
class EventThread(QThread):
    getTasks = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.isLive = True
        self.tasks = []
    @pysnooper.snoop(output=f"./debug/debug1{time.time()}.log")
    def run(self):
        while self.isLive:
            self.getTasks.emit(self)
            # logger.debug("")
            # pprint(self.tasks)
            for task in self.tasks:
                if task.condition():
                    task.func()

    def stop(self):
        self.isLive = False
        self.quit()
        self.wait()

#
#
# class NLPthread(QThread):
#     runNLP = pyqtSignal(dict)
#
#     def __init__(self):
#         super().__init__()
#         self.isLive = True
#         self.task = []
#
#     def addTask(self, dict):
#         self.task.append(dict)
#
#     def run(self):
#         self.generator = AI.generator(self)
#         self.generator.init()
#         while self.isLive:
#             for task in self.task:
#                 result = self.generator.generateText(task["text"])
#                 task['parent'].returnSignal.emit(result[0]["text"])  # type: ignore
#                 self.task.remove(task)
#             self.exec()
#
#     def stop(self):
#         self.isLive = False
#         self.quit()
#         self.wait()

#
# class MoveThread(QThread):
#     addLogic = pyqtSignal(list)
#
#     def __init__(self):
#         super().__init__()
#         self.logics = {}
#         self.isLive = True
#         self.main = None
#         signalBin.signalBin.getMain.emit(self)
#
#     def addLogic_(self, logics: signalBin.Logic):
#         for logic in logics:
#             if logic.type == "toResult":
#                 # self.logics[logic.pet.id].extend(signalBin.changeToProcess(logic))
#                 for logic_ in signalBin.changeToProcess(logic):
#                     self.logics[logic.pet.id].append(logic_)
#
#                 # logger.warning("add logic to result")
#             else:
#                 self.logics[logic.pet.id].append(logic)
#
#     # @pysnooper.snoop(thread_info=True,prefix="move thread run func:")
#     def run(self):
#         for pet in self.main.pets:
#             self.logics[pet.id] = []
#         logger.info("move thread start")
#         while self.isLive:
#             QCoreApplication.processEvents()
#             for pet in self.main.pets:  # type: ignore
#                 if pet.active:
#                     if self.logics[pet.id]:
#                         logic = self.logics[pet.id][0]
#                         if logic.speed > logic.distence:
#                             pet.moveSignal.emit(logic.direction, logic.distence)
#                             logger.debug("moveSignal emit")
#                         else:
#                             pet.moveSignal.emit(logic.direction, logic.speed)
#                             logger.debug("moveSignal emit")
#             logger.debug("move thread running")
#
#     def stop(self):
#         self.isLive = False
#         self.quit()
#         self.wait()


class Main(QWidget):
    addTaskSignal = pyqtSignal(QThread)

    def __init__(self):
        logger.info("all init start")
        self.app = QApplication(sys.argv)
        QtWidgets.QWidget.__init__(self)
        # self.threadPool = ThreadPoolExecutor(max_workers=10)  #

        self.pets = []
        self.taskList = []
        self.eventList = []
        self.setGetSignal()
        self.initEventThread()
        self.initTask()
        # self.initTimerThread()
        self.initPets()
        # self.initMoveThread()
        # self.initGenerator()
        self.initCtrlWindow()
        self.initSysMenu()


    def initEventThread(self):
        self.eventThread = EventThread()

        def getEventList(obj):
            obj.tasks.extend(self.eventList)

            # logger.debug(f"getEventList,{self.eventList}\n{obj.task}")
        self.eventThread.getTasks.connect(getEventList)
        self.eventThread.start()

    def initTask(self):
        self.addTaskSignal.connect(self.addTask)

    def addTask(self, task):
        self.taskList.append(task)
        task.start()

    #
    # def initGenerator(self):
    #     self.NLPthread = NLPthread()
    #
    #     self.NLPthread.runNLP.connect(lambda dict: self.NLPthread.addTask(dict))
    #     self.NLPthread.start()
    #     logger.info("NLP started")
    #
    # def initMoveThread(self):
    #     self.MoveThread = MoveThread()
    #
    #     self.MoveThread.addLogic.connect(lambda list: self.MoveThread.addLogic_(list))
    #     self.MoveThread.start()
    #     logger.info("Move started")
    #
    # def initTimerThread(self):
    #     self.timerThread = MainTimerThread()
    #     self.timerThread.setTimerFuncs.connect(lambda func, cmd: self.timerThread.setTimerFunc(func, cmd))
    #     self.timerThread.start()
    #     logger.info("timer started")

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

    def quit(self):
        self.app.quit()
        self.timerThread.stop()

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
