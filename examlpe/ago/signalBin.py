import random

from PyQt5.QtCore import QObject, pyqtSignal
from dataclasses import dataclass
from loguru import logger


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
    func: object
    parent: object
    condition: object = lambda: True
    id: str = str(random.randint(10000000, 99999999))


class task(object):
    def __init__(self, type):
        self.type = type

    def run(self):
        pass


@dataclass
class logic_move_to_endpoint:
    pet: object
    endpoint: pos = pos()
    speed: float = 0.0
    type: str = "move_endpoint"


@dataclass
class logic_move_step:
    pet: object
    distance: float = 0.0
    direction: str = "east"
    speed: float = 0.0
    type: str = "move_step"


def changeTo_move_step(self):
    nowPos = self.pet.nowPos
    # logger.warning("changeToProcess logic")
    return [
        logic_move_step(
            self.pet,
            abs(nowPos.x - self.endpoint.x),
            {True: "west", False: "east"}[nowPos.x > self.endpoint.x],
            self.speed,
            "move_step",
        ),
        logic_move_step(
            self.pet,
            abs(nowPos.y - self.endpoint.y),
            {True: "north", False: "south"}[nowPos.y > self.endpoint.y],
            self.speed,
            "move_step"
        )
    ]


@dataclass
class logic_put:
    pet: object
    block: object = None
    pos: pos = pos()
    type: str = "put"


@dataclass
class logic_break:
    pet: object
    block: object = None
    pos: pos = pos()
    type: str = "break"


class result(object):
    def __init__(self, info):
        self.info = info


class SignalBin(QObject):
    getMain = pyqtSignal(object)
    getValues = pyqtSignal()


signalBin = SignalBin()
