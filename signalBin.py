from PyQt5.QtCore import QObject, pyqtSignal


class SignalBin(QObject):
    getMain = pyqtSignal(object)
    getValues=pyqtSignal()

signalBin=SignalBin()