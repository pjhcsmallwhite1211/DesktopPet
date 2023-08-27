
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow
from NLP import Generator,NLPThread  
from libs import *
import Desktop_Pet
import petC
import libs
class System(object):
    def __init__(self):
        self.pet:list[petC.Pet]=[]
        self.timer = QTimer()
        self.timer.timeout.connect(self.awaken)
        self.timer.start(1)
    def awaken(self):
        for i in self.pet:
            if i.isLive:
                # logger.info(f"{i.id} awaken,tasks:{i.taskList}")
                i.awaken()
    def initPet(self):
        for i in range(7):
            self.pet.append(petC.Pet(i,i))
        self.hide(-1)
    def changePetItem(self,pet,item):
        if type(pet)==int:
            self.pet[pet].changeItem(item)
        elif type(pet)==petC.Pet:
            pet.changeItem(item)
        else:
            raise TypeError('"pet"arg must be int or petC.Pet')
    def changePetFace(self, pet, face):
        if type(pet)==int:
            self.pet[pet].changeFace(face)
        elif type(pet)==petC.Pet:
            pet.changeFace(face)
        else:
            raise TypeError('"pet"arg must be int or petC.Pet')
    def changePetFeet(self, pet, feet):
        if type(pet)==int:
            self.pet[pet].changeFeet(feet)
        elif type(pet)==petC.Pet:
            pet.changeFeet(feet)
        else:
            raise TypeError('"pet"arg must be int or petC.Pet')
    def hide(self,index):
        if index<0:
            for i in self.pet:
                i.hide()
        elif 0<index<7:
            self.pet[index].hide()
        else:
            raise IndexError('"index"arg must be 0<index<7')
    def show(self,index):
        if index<0:
            for i in self.pet:
                i.show()
        elif 0<index<7:
            self.pet[index].show()
        else:
            raise IndexError('"index"arg must be 0<index<7')

class controlPanel(object):
    def __init__(self):
        
        self.mainWindow = QMainWindow()
        self.ui = Desktop_Pet.Ui_MainWindow()
        self.ui.setupUi(self.mainWindow)
        self.mainWindow.show()
        self.system=System()
        self.system.initPet()
        self.isLive=False
        self.nowPet=self.system.pet[self.ui.toolBox.currentIndex()]
        self.initEvent()
        self.ui.toolBox.currentChanged.connect(self.getNowPet) # type: ignore

    def getNowPet(self):
        self.nowPet = self.system.pet[self.ui.toolBox.currentIndex()]
        return self.nowPet
    
    def initEvent(self):
        self.getNowPet()
        width:int = getattr(libs.values,'SCREEN_WIDTH')
        height:int = getattr(libs.values,"SCREEN_HEIGHT")
        home:pos = getattr(libs.values,"HOME")
        center:pos  = getattr(libs.values,"CENTER")
        images:list[str] = getattr(libs.values,"IMAGES")
        self.ui.apple.clicked.connect(lambda: self.nowPet.changeItem("apple"))  #
        self.ui.pickaxe.clicked.connect(lambda: self.nowPet.changeItem("diamond_pickaxe"))  #
        self.ui.compass.clicked.connect(lambda: self.nowPet.changeItem("compass_18"))  #
        self.ui.bread.clicked.connect(lambda: self.nowPet.changeItem("bread"))  #
        self.ui.random.clicked.connect(lambda: self.nowPet.changeItem(random.choice(images)))  #
        self.ui.moveToHome_Button.clicked.connect(lambda: self.nowPet.move(home))  #
        self.ui.moveToRandomPos_button.clicked.connect(lambda: self.nowPet.move(
            # 随机移动位置
            pos(random.randint(0, int(width)), random.randint(0, int(height)))))
        # 把主界面移到屏幕底部
        self.ui.moveToTheBottomOfTheScreen_button.clicked.connect(
            lambda: self.nowPet.move(pos(self.nowPet.pos.x,height-50))) # type: ignore
        # 把主界面移到屏幕中央
        self.ui.moveToTheCenterOfTheScreen_button.clicked.connect(
            lambda: self.nowPet.move(center))
        
        self.ui.east.clicked.connect(lambda: self.nowPet.taskList.append(task(self.nowPet.moveTaskFunction,lambda task :task.infos["distance"]<=0 ,type="move_step",speed=2,direction="east",distance=int(self.ui.nSteps.text()),tag="user")))
        self.ui.west.clicked.connect(lambda: self.nowPet.taskList.append(task(self.nowPet.moveTaskFunction,lambda task :task.infos["distance"]<=0 ,type="move_step",speed=2,direction="west",distance=int(self.ui.nSteps.text()),tag="user")))
        self.ui.north.clicked.connect(lambda: self.nowPet.taskList.append(task(self.nowPet.moveTaskFunction,lambda task :task.infos["distance"]<=0 ,type="move_step",speed=2,direction="north",distance=int(self.ui.nSteps.text()),tag="user")))
        self.ui.south.clicked.connect(lambda: self.nowPet.taskList.append(task(self.nowPet.moveTaskFunction,lambda task :task.infos["distance"]<=0 ,type="move_step",speed=2,direction="south",distance=int(self.ui.nSteps.text()),tag="user")))
        self.ui.nSteps.setText("200")
        self.ui.goHome.clicked.connect(lambda: self.nowPet.hide())
        self.ui.goOut.clicked.connect(lambda: self.nowPet.show())
        self.ui.clearTask.clicked.connect(lambda: self.nowPet.taskList.clear())

        self.ui.status.activated.connect(lambda: self.nowPet.changeStatus(
            {"原地站立": "stand", "玩耍状态": "playMode"}[self.ui.status.currentText()]))
        self.nowPet.changeStatus("stand")
    def show(self):
        self.isLive=True
        self.mainWindow.show()
    def hide(self):
        self.isLive=False
        self.mainWindow.hide()

