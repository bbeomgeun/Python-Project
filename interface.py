# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(340, 161)
        self.pushbtn = QtWidgets.QPushButton(Form)
        self.pushbtn.setGeometry(QtCore.QRect(250, 30, 61, 101))
        self.pushbtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushbtn.setObjectName("pushbtn")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(43, 34, 151, 91))
        self.label.setStyleSheet("background-color : black;\n"
"color : white;")
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushbtn.setText(_translate("Form", "중지"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

