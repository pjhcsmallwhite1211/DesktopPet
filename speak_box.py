# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'speak_box.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(291, 125)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/image/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.box_r = QtWidgets.QLabel(Form)
        self.box_r.setGeometry(QtCore.QRect(240, 20, 20, 80))
        self.box_r.setText("")
        self.box_r.setPixmap(QtGui.QPixmap(":/ui/image/speak_box_r_h.png"))
        self.box_r.setScaledContents(True)
        self.box_r.setObjectName("box_r")
        self.box_l = QtWidgets.QLabel(Form)
        self.box_l.setGeometry(QtCore.QRect(20, 20, 21, 80))
        self.box_l.setText("")
        self.box_l.setPixmap(QtGui.QPixmap(":/ui/image/speak_box_l_h.png"))
        self.box_l.setScaledContents(True)
        self.box_l.setObjectName("box_l")
        self.box_b = QtWidgets.QLabel(Form)
        self.box_b.setGeometry(QtCore.QRect(39, 20, 201, 80))
        self.box_b.setText("")
        self.box_b.setPixmap(QtGui.QPixmap(":/ui/image/speak_box.png"))
        self.box_b.setScaledContents(True)
        self.box_b.setObjectName("box_b")
        self.text = QtWidgets.QLabel(Form)
        self.text.setGeometry(QtCore.QRect(40, 28, 201, 56))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.text.setFont(font)
        self.text.setStyleSheet("color: rgb(0, 0, 255);")
        self.text.setMidLineWidth(11)
        self.text.setTextFormat(QtCore.Qt.MarkdownText)
        self.text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.text.setWordWrap(True)
        self.text.setObjectName("text")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.text.setText(_translate("Form", "askdjijaiooooisdijaijdijoajaodijsijaoijdoiajo"))
import test_rc