import random
import time

from PyQt5.QtCore import QObject, pyqtSignal, QTimer


# 定义 NPC 类，表示游戏中的一个非玩家角色
class AI(QObject):
    putBlocks = pyqtSignal(str, list)

    def __init__(self, args):
        super().__init__()

        # 创建 NPC 实例
        self.npc = NPCAI()
        self.npc.args = [self, args["arg"]]
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
        self.npc.add_node(Walk())
        # self.timer=QTimer()
        # self.timer.setInterval(200)
        # self.timer.timeout.connect(self.run)
        # self.timer.start()
        self.running = True
        self.runable = True

    def run(self):
        while self.runable:
            # print("dasdadafoooo")
            if self.running == False:
                # print("spppppp")
                continue

            time.sleep(0.02)
            self.npc.update()
            # print("ksko")
    #
    # def run(self):
    #     self.npc.update()

class NPCAI(object):
    def __init__(self):
        super(NPCAI, self).__init__()
        self.args = None
        self.behavior_tree = []  # NPC 的行为树，初始为空列表

    # 添加节点到 NPC 的行为树中
    def add_node(self, node):
        self.behavior_tree.append(node)

    # 更新 NPC 的行为树
    def update(self):
        for node in self.behavior_tree:
            if node.execute(self.args) == "success":  # 如果某个节点执行成功，则停止更新行为树
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
    def execute(self, a=0):
        for child in self.children:
            if child.execute() == "success":  # 如果某个子节点执行成功，则返回成功
                return "success"
        return "failure"  # 所有子节点都执行失败，则返回失败


# 定义序列器节点，用于按照顺序执行子节点
class Sequence(Node):
    def execute(self, a=9):
        for child in self.children:
            if child.execute() == "failure":  # 如果某个子节点执行失败，则返回失败
                return "failure"
        return "success"  # 所有子节点都执行成功，则返回成功


# 定义任务接受节点，用于判断是否需要接受任务，并执行相应的操作
class PutBlocks(Node):
    def execute(self, l):
        if random.randint(1, 100) == 2:  # 判断是否有任务需要接受
            self.putBlock(l)  # 如果需要，接受任务
            return "success"  # 返回成功
        return "failure"  # 否则返回失败

    def putBlock(self, l):
        putBlockSignal_ = l[0]
        deskTopPet = l[1]
        putBlockSignal_.putBlocks.emit(deskTopPet.randomItem(),
                                       [random.randint(0, 29) * 64, random.randint(0, 16) * 64])
        print("p")


class Walk(Node):
    def execute(self, l):
        deskTopPet = l[1]
        pet = deskTopPet.pet
        print("sdad")
        if random.randint(0, 20) == 0:
            pet.moveStep(random.choice(["west", "east", "north", "south"]), random.randint(30, 200))
            return "success"  # 返回成功
        return "failure"  # 返回失败
