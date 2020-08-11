
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton, QCheckBox, QProgressBar, QLineEdit, QWidget
from PyQt5.QtCore import QDate, Qt
import time
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QCheckBox,QGridLayout



class QtGUI(QWidget):

    def __init__(self):
        super().__init__()
        self.num = 0
        self.setWindowTitle("Appia Qt GUI")
        
        self.resize(500, 500)
        self.qclist = []
        self.position = 0
        self.Lgrid = QGridLayout()
        self.setLayout(self.Lgrid)
        self.lineedit = QLineEdit(self)
        self.Lgrid.addWidget(self.lineedit,10,0)
        addbutton = QPushButton('Add Item',self)
        self.Lgrid.addWidget(addbutton,10,1)
        self.conn = sqlite3.connect("mydb.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM todo;")
        self.rows = self.cur.fetchall()
        for self.row in self.rows:
            if self.row[2] == "1":
                # qc1 = QCheckBox(self.row[0], self)
                # qcb = QPushButton("Del..",self)
                # qcp = QProgressBar()
                # qcp.setValue(5)
                # self.Lgrid.addWidget(qc1,self.position,0)
                # self.Lgrid.addWidget(qcp,self.position,1)
                # self.Lgrid.addWidget(qcb,self.position,2)

                # self.position = self.position + 1
                self.addWidget(self.row[0])
        # addbutton.clicked.connect( self.add_item)
        self.show()

    def addWidget(self, text):
        qc1 = QCheckBox(text, self)
        qcb = QPushButton("Del..",self)
        qcp = QProgressBar()
        qcp.setValue(5)
        self.Lgrid.addWidget(qc1,self.position,0)
        self.Lgrid.addWidget(qcp,self.position,1)
        self.Lgrid.addWidget(qcb,self.position,2)
        self.position = self.position + 1
        qcb.clicked.connect(lambda:self.del_qcbox(qc1, qcb, qcp))

    def del_qcbox(self,qc1, qcb, qcp):
        qc1.deleteLater()
        qcb.deleteLater()
        qcp.deleteLater()
        self.position = self.position - 1
        # for self.i in reversed(range(self.Lgrid.count())): 
        #     self.Lgrid.itemAt(self.i).widget().setParent(None)

    # def update()



if __name__ == '__main__':

    app = QApplication(sys.argv)

    ex = QtGUI()

    app.exec_()

    # def updateGrid(self, taskList):

       # delete existing items from grid
    #    for i in reversed(range(self.my_grid.count())):
    #        widgetToRemove = self.my_grid.itemAt(i).widget()
    #        widgetToRemove.setParent(None)
    #        widgetToRemove.deleteLater()

    #    # add new buttons
    #    for task in tasklist:
    #        btn = QPushButton(task)
    #        self.my_grid.addWidget(btn)
