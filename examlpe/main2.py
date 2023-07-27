# 导入模块
import os  # 包含操作系统相应的功能
import random  # 生成随机数
import sys  # 提供了对 Python 解释器进行访问和一些与解释器强烈交互的变量和函数
import time
from concurrent.futures import ThreadPoolExecutor  # 支持多线程
from dataclasses import dataclass  # 引入数据类，可以快速创建一个类

from PyQt5 import Qt  # PyQt5 相关
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow  # PyQt5 相关组件
from pyqt5_plugins.examplebuttonplugin import QtGui  # 自定义的插件

from examlpe.ago import Desktop_Pet, block
import pet  # 导入自定义模块

app = QApplication(sys.argv)  # 创建 QApplication 实例

threadPool = ThreadPoolExecutor(max_workers=5)  # 创建5个线程


# 定义 NPC 类，表示游戏中的一个非玩家角色
class PutBlockSignal(QObject):
    putBlocks = pyqtSignal(str, list)

    def __init__(self):
        super().__init__()

        # 创建 NPC 实例
        self.npc = NPCAI()
        # 创建选择器节点和序列器节点
        self.selector1 = Selector()
        self.selector2 = Selector()

        # 将选择器节点和序列器节点添加到 NPC 的行为树中
        self.npc.add_node(self.selector1)
        self.selector1.add_child(self.selector2)
        #
        # # 创建任务接受节点和提供信息节点，并将它们添加到序列器节点中
        # selector2.add_child(AcceptTask())
        # selector2.add_child(ProvideInfo())

        # 创建询问节点，并将它添加到 NPC 的行为树中
        self.npc.add_node(PutBlocks())

    def run(self):
        while running:
            try:
                time.sleep(0.1)
                self.npc.update()
            except Exception as e:
                print(e)


class NPCAI(object):
    def __init__(self):
        super(NPCAI, self).__init__()

        self.behavior_tree = []  # NPC 的行为树，初始为空列表

    # 添加节点到 NPC 的行为树中
    def add_node(self, node):
        self.behavior_tree.append(node)

    # 更新 NPC 的行为树
    def update(self):
        for node in self.behavior_tree:
            if node.execute() == "success":  # 如果某个节点执行成功，则停止更新行为树
                print("successfully")
                return


# 定义行为树节点基类，所有节点都是其子类
class Node:
    def __init__(self):
        self.children = []  # 节点的子节点列表

    # 添加子节点到节点的子节点列表中
    def add_child(self, child):
        self.children.append(child)


# 定义选择器节点，用于从多个子节点中选择一个执行
class Selector(Node):
    def execute(self):
        for child in self.children:
            if child.execute() == "success":  # 如果某个子节点执行成功，则返回成功
                return "success"
        return "failure"  # 所有子节点都执行失败，则返回失败


# 定义序列器节点，用于按照顺序执行子节点
class Sequence(Node):
    def execute(self):
        for child in self.children:
            if child.execute() == "failure":  # 如果某个子节点执行失败，则返回失败
                return "failure"
        return "success"  # 所有子节点都执行成功，则返回成功


# 定义任务接受节点，用于判断是否需要接受任务，并执行相应的操作
class PutBlocks(Node):
    def execute(self):
        if random.randint(1, 10) == 2:  # 判断是否有任务需要接受
            self.putBlock()  # 如果需要，接受任务
            return "success"  # 返回成功
        return "failure"  # 否则返回失败

    def putBlock(self):
        putBlockSignal_.putBlocks.emit(deskTopPet.randomItem(),
                                       [random.randint(0, 29) * 64, random.randint(0, 16) * 64])


#
# # 定义提供信息节点，用于判断是否需要提供任务相关的信息，并执行相应的操作
# class ProvideInfo(Node):
#     def execute(self):
#         if has_task() and task_info_needed():  # 判断是否需要提供信息
#             provide_info()  # 如果需要，提供信息
#             return "success"  # 返回成功
#         return "failure"  # 否则返回失败
#
# # 定义询问节点，用于向玩家询问任务相关的信息，并执行相应的操作
# class Ask(Node):
#     def execute(self):
#         if has_task():  # 判断是否有任务需要询问
#             ask()  # 如果需要，向玩家询问信息
#             return "success"  # 返回成功
#         return "failure"  # 否则返回失败


class Value(object):
    """
    用于存储屏幕的大小信息
    """
    # 获取屏幕大小
    screenRect = app.desktop()
    screenSize = screenRect.size()
    width = screenSize.width()
    height = screenSize.height()


value = Value()


class DesktopPet(object):
    """
    桌宠主界面相关的操作
    """

    def __init__(self):
        pass

    def itemButtonClicked(self, item):
        """
        切换 item 图片
        """
        ui.item.setPixmap(QtGui.QPixmap(f":/image/image/{item}"))  # 切换 item 图片
        ui2.item.setPixmap(QtGui.QPixmap(f":/image/image/{item}"))

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

    def main1(self):
        """
        绑定各个按钮的点击事件
        """
        ui.apple.clicked.connect(lambda: self.itemButtonClicked("apple.png"))
        ui.pickaxe.clicked.connect(lambda: self.itemButtonClicked("diamond_pickaxe.png"))
        ui.compass.clicked.connect(lambda: self.itemButtonClicked("compass_18.png"))
        ui.bread.clicked.connect(lambda: self.itemButtonClicked("bread.png"))
        ui.random.clicked.connect(lambda: self.itemButtonClicked(self.randomItem()))
        ui.moveToHome_Button.clicked.connect(lambda: pet.moveMainWindow2(pet.home))
        ui.moveToRandomPos_button.clicked.connect(lambda: pet.moveMainWindow2(
            # 随机移动位置
            pet.pos(random.randint(0, int(value.width)), random.randint(0, int(value.height)))))
        # 把主界面移到屏幕底部
        ui.moveToTheBottomOfTheScreen_button.clicked.connect(lambda: pet.moveMainWindow2(pet.bottomPosUpdata()))
        # 把主界面移到屏幕中央
        ui.moveToTheCenterOfTheScreen_button.clicked.connect(lambda: pet.moveMainWindow2(pet.center))
        ui.east.clicked.connect(lambda: pet.moveStep("east", int(ui.nSteps.text())))
        ui.west.clicked.connect(lambda: pet.moveStep("west", int(ui.nSteps.text())))
        ui.north.clicked.connect(lambda: pet.moveStep("north", int(ui.nSteps.text())))
        ui.south.clicked.connect(lambda: pet.moveStep("south", int(ui.nSteps.text())))
        ui.nSteps.setText("200")


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

    def moveMainWindow2(self, pos):
        """
        移动主界面到指定位置
        """
        mainWindow2.move(pos.x, pos.y)

    def moveStep(self, forward, distance):
        """
        根据方向和距离移动指定的步数
        """
        print('kdosakdpokapokfpospgpanh;sdvmskmdvkk')
        match forward:
            case "north":  # 向北走
                for i in range(distance):
                    self.nowPos.y -= 1
                    mainWindow2.move(self.nowPos.x, self.nowPos.y)  # 移动主界面
            case "south":  # 向南走
                for i in range(distance):
                    self.nowPos.y += 1
                    mainWindow2.move(self.nowPos.x, self.nowPos.y)
            case "east":  # 向东走
                for i in range(distance):
                    self.nowPos.x += 1
                    mainWindow2.move(self.nowPos.x, self.nowPos.y)
            case "west":  # 向西走
                for i in range(distance):
                    self.nowPos.x -= 1
                    mainWindow2.move(self.nowPos.x, self.nowPos.y)

    def main2(self):
        """
        辅助窗口的风格和样式
        """
        mainWindow2.setWindowFlags(Qt.Qt.FramelessWindowHint)  # 设置辅助窗口无边框
        mainWindow2.setAttribute(Qt.Qt.WA_TranslucentBackground)  # 设置透明背景


class BlockList(object):
    class Block(object):
        def __init__(self):
            self.window = None
            self.ui = None
            self.pos = None

        def __repr__(self):
            return f'<Block window={self.window},ui={self.ui}>'

    def __init__(self):
        self.blockList = []

    def add(self, block):
        self.blockList.append(block)


blockList_ = BlockList()


def showWindow(str, pos):
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
    blockList_.add(block_)


putBlockSignal_ = PutBlockSignal()
putBlockSignal_.putBlocks.connect(showWindow)
running = True
threadA = threadPool.submit(putBlockSignal_.run, )
mainWindow = QMainWindow()
ui = Desktop_Pet.Ui_MainWindow()  # 使用 PyQt5 Designer 设计的 UI 界面
ui.setupUi(mainWindow)
deskTopPet = DesktopPet()
deskTopPet.main1()  # 绑定各个按钮的点击事件
# threadB = threadPool.submit(deskTopPet.main1)
mainWindow.show()

mainWindow2 = QMainWindow()
ui2 = pet.Ui_Form()  # 使用 PyQt5 Designer 设计的 UI 界面
ui2.setupUi(mainWindow2)
pet = Pet()
# threadC = threadPool.submit(pet.main2)
pet.main2()  # 辅助窗口的风格和样式
mainWindow2.show()


def closeEvent(self):
    global running
    running = False


mainWindow2.closeEvent = closeEvent
# threadPool.shutdown()
print('hello')

sys.exit(app.exec_())  # 执行 QApplication 实例并退出程序
