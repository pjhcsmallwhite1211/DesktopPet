import speak_box
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QTextCursor
from PyQt5.QtCore import pyqtSignal, QObject, QThread

class speakBox(object):
    def __init__(self):
        
        self.mainWindow = QMainWindow()
        self.ui = speak_box.Ui_Form()
        self.ui.setupUi(self.mainWindow)
        self.isLive=False
        self.text = ""
    def show(self):
        self.isLive=True
        self.mainWindow.show()
    def hide(self):
        self.isLive=False
        self.mainWindow.hide()
    def addText(self, text):
        self.text+=text
        self.ui.textEdit.setText(self.text)
        self.ui.textEdit.moveCursor(QTextCursor.End)
    def setText(self,text):
        self.text=text
        self.ui.textEdit.setText(self.text)
        self.ui.textEdit.moveCursor(QTextCursor.End)
    