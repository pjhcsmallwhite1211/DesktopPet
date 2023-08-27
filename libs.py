import os
import random
from PyQt5.QtWidgets import QMainWindow

from PyQt5.QtCore import QObject, pyqtSignal
from dataclasses import dataclass
from loguru import logger
from NLP import NLPSystem
import rect___

@dataclass
class pos:
    """
    主界面坐标信息
    """

    x: float = 0
    y: float = 0


@dataclass
class rect:
    left_top_x: float
    left_top_y: float
    right_bottom_x: float
    right_bottom_y: float


@dataclass
class Func:
    run: object
    args:tuple = ()
    parent: object=None
    condition: object = lambda: True
    id: str = str(random.randint(10000000, 99999999))

@dataclass
class Values:
    pass

class SignalBin(QObject):
    pass

signalBin = SignalBin()
values = Values()
# 使用递归遍历资源文件夹，把所有图片存放在列表中
def forDir(path_,list):
    for path, childDir, files in os.walk(path_):
        if not childDir:  # 遍历到底层目录
            list.extend(files)
        else:
            forDir(path + "/" + childDir[0],list)  # 沿着子目录递归遍历
def inRect(pet,rect):
    if (
            rect.left_top_x <= pet.pos.x <= rect.right_bottom_x
            and rect.left_top_y <= pet.pos.y <= rect.right_bottom_y
    ):
        return True
    return False
def changeTo_move_step(task_,pet):
    nowPos = pet.pos
    # logger.warning("changeToProcess logic")
    # type="move_step",speed=2,direction="east",distance=int(self.ui.nSteps.text())
    listc=[
        task(task_.run_,task_.ifRemove,type='move_step',
             speed=task_.infos['speed'],
             direction={True: "north", False: "south"}[nowPos.y > task_.infos["endpoint"].y],
             distance=abs(nowPos.y - task_.infos["endpoint"].y),
             tag=task_.infos["tag"]

            ),
        task(task_.run_,task_.ifRemove,type='move_step',
             speed=task_.infos['speed'],
             direction={True: "west", False: "east"}[nowPos.x > task_.infos["endpoint"].x],
             distance=abs(nowPos.x - task_.infos["endpoint"].x),
             tag=task_.infos["tag"]

            )
        ]
    indexc=random.randint(0,1)  
    return [listc[indexc],listc[indexc-1]]
class task(object):
    def __init__ (self,run_,ifRemove=lambda i: False,**infos):
        self.infos = infos
        self.run_ = run_
        self.ifRemove = ifRemove

    def __str__(self):
        return f"task(run_={self.run_},infos={self.infos}"
    def __repr__(self):
        return f"task(run_={self.run_},infos={self.infos}"
class rect_show(object):
    def __init__(self,rect_:rect):
        self.mainWindow = QMainWindow()
        self.ui = rect___.Ui_Form()
        self.ui.setupUi(self.mainWindow)
        self.mainWindow.show()
        self.mainWindow.resize(int(rect_.left_top_x-rect_.right_bottom_x), int(rect_.left_top_y-rect_.right_bottom_y))
        logger.debug("aokspodpoas")
        self.mainWindow.move(int(rect_.left_top_x), int(rect_.left_top_y))

# @dataclass
# class logic_move_to_endpoint:
#     pet: object
#     endpoint: pos = pos()
#     speed: float = 0.0
#     type: str = "move_endpoint"


# @dataclass
# class logic_move_step:
#     pet: object
#     distance: float = 0.0
#     direction: str = "east"
#     speed: float = 0.0
#     type: str = "move_step"


# def changeTo_move_step(self):
#     nowPos = self.pet.nowPos
#     # logger.warning("changeToProcess logic")
#     return [
#         logic_move_step(
#             self.pet,
#             abs(nowPos.x - self.endpoint.x),
#             {True: "west", False: "east"}[nowPos.x > self.endpoint.x],
#             self.speed,
#             "move_step",
#         ),
#         logic_move_step(
#             self.pet,
#             abs(nowPos.y - self.endpoint.y),
#             {True: "north", False: "south"}[nowPos.y > self.endpoint.y],
#             self.speed,
#             "move_step"
#         )
#     ]


# @dataclass
# class logic_put:
#     pet: object
#     block: object = None
#     pos: pos = pos()
#     type: str = "put"


# @dataclass
# class logic_break:
#     pet: object
#     block: object = None
#     pos: pos = pos()
#     type: str = "break"


# class result(object):
#     def __init__(self, info):
#         self.info = info