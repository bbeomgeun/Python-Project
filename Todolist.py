from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton, QCheckBox, QProgressBar, QLineEdit, QWidget, QGridLayout
from PyQt5.QtCore import QDate, Qt
import MainTodo_ver1
import time
import sqlite3

class login_Page():
    def __init__(self, ui):
        self.errorCount = 0
        self.result = 0
        self.conn = sqlite3.connect("mydb.db")
        self.cur = self.conn.cursor()
        self.window = ui
        self.window.stackedWidget.setCurrentWidget(self.window.page1_login)
        self.window.Button_LogIn.clicked.connect(self.LoginFunction)
        self.window.Button_register.clicked.connect(self.RegisterFunction)
        # 비밀번호 *으로 바꾸기(setEchoMode)
        self.window.text_PW.setEchoMode(2)

        #self.window.text_hello.setText(self.ID + "님 안녕하세요!")

    def LoginFunction(self):
        print("clicked")
        self.ID = self.window.text_ID.text()
        self.PW = self.window.text_PW.text()
        self.cur.execute("SELECT * FROM user;")
        self.rows = self.cur.fetchall()

        for self.row in self.rows:
            if self.ID == self.row[0]:
                self.result = 1
                if self.PW == self.row[1]:
                    self.result = 2
                    break

        if self.result == 0:
            self.window.text_status.setText("존재하지 않는 ID입니다. \n회원가입 하시겠습니까?")
            # self.reqly = QMessageBox.question(self, 'Message', '회원가입 하시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            # if reply == QMessageBox.Yes:
            #     self.window.stackedWidget.setCurrentWidget(self.window.page6_register)
            # else:
            #     self.window.stackedWidget.setCurrentWidget(self.window.page1_login)
        
        elif self.result == 1:
            self.window.text_status.setText("비밀번호가 일치하지 않습니다")
            self.errorCount += 1
            if self.errorCount < 5:
                self.window.text_status.setText("로그인" + str(self.errorCount) + "회 오류\n5회 이상 오류시 프로그램이 종료됩니다.")
            elif self.errorCount == 5:
                ####Qmessagebox로 경고창
                self.window.text_status.setText("종료됩니다.")
                self.window.stackedWidget.setCurrentWidget(self.window.page7_onedayResult)
        elif self.result == 2:
            self.window.stackedWidget.setCurrentWidget(self.window.page2_main)

    def RegisterFunction(self):
        self.window.stackedWidget.setCurrentWidget(self.window.page6_register)
        self.window.register_save.clicked.connect(self.register)

    def register(self):
        self.cur.execute("SELECT * FROM user;")
        self.rows = self.cur.fetchall()
        self.newID = self.window.register_ID.text()
        self.newPW = self.window.register_PW.text()
        self.infoResultID = 0
        self.infoResultPW = 0

        for self.row in self.rows:
            if self.newID == self.row[0]:
                self.infoResultID = 1

        if self.infoResultID == 1:
            self.window.id_warning.setText("이미 등록된 ID입니다. \n다시 입력해주세요.")

        if len(self.newPW)<4:
            self.window.pw_warning.setText("4글자 이상 설정해주세요.")
            self.infoResultPW = 1

        if self.infoResultID == 0 & self.infoResultPW == 0:
            # self.window.id_warning.setText("사용가능합니다.")
            self.cur.execute("INSERT INTO user VALUES('"+self.newID+"',"+"'"+self.newPW+"');")
            self.conn.commit()
            self.window.stackedWidget.setCurrentWidget(self.window.page1_login)
##########################################################################################
class stack_Page():
    def __init__(self, ui):
        self.window = ui
        self.window.button_finish.clicked.connect(self.ToFinish)
        self.window.button_setting.clicked.connect(self.ToSetting)
        self.window.button_add.clicked.connect(self.ToAdd)

        self.window.page3_toMain.clicked.connect(self.ToMain)
        self.window.page4_toMain.clicked.connect(self.ToMain)
        self.window.page5_toMain.clicked.connect(self.ToMain)
        self.window.date_save.clicked.connect(self.ToMain)

    def ToMain(self):
        self.window.stackedWidget.setCurrentWidget(self.window.page2_main)

    def ToFinish(self):
        self.window.stackedWidget.setCurrentWidget(self.window.page3_finish)

    def ToSetting(self):
        self.window.stackedWidget.setCurrentWidget(self.window.page4_setting)

    def ToAdd(self):
        self.window.stackedWidget.setCurrentWidget(self.window.page5_add)
###########################################################################################

class TodoList(QWidget):
    def __init__(self, ui):
        super().__init__()

        self.window = ui
        self.window.stackedWidget.setCurrentWidget(self.window.page1_login)
        self.position = 0
        self.finish_position = 0
        self.conn = sqlite3.connect("mydb.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM todo;")
        self.rows = self.cur.fetchall()

        for self.row in self.rows:
            if self.row[2] == "1":
                self.add_todo(self.row[0], self.row[1])

        self.window.button_finish.clicked.connect(lambda : self.updateUI_finish()) #완료버튼시 finish_gridlayout update
        self.window.page3_toMain.clicked.connect(lambda : self.updateUI_main()) #메인버튼시 mainlayout update
    
    def add_todo(self, text, date):
        self.current = QDate.currentDate()
        self.dday = QDate.fromString(date, "yyyy-MM-dd")
        self.interval = self.current.daysTo(self.dday)
        self.progressbarValue = 100-self.interval # progressbar는 value에 맞춰서 그래픽이 구현 -> d-day는 남은 날짜로 그래프진행상태 표시이므로 빼준다
        chkbtn = QPushButton(text, self)
        qcp = QProgressBar(self)
        btn = QPushButton("Del..",self)
        qcp.setValue(self.progressbarValue) 
        qcp.setFormat(str(self.interval) + "-DAY") # 실제 표시해주는 data는 interval 그대로
        if (self.interval <= 5):                #d-day(interval)이 5일 이내라면 붉은색으로
            qcp.setStyleSheet("QProgressBar::chunk {background-color : red;}") # stylesheet 바꿔준다.
            ## d-day가 표시되던 defaultFormat이 깨진다(색을 바꿨더니) -> 고치기
        self.window.main_GridLayout.addWidget(chkbtn,self.position,0)
        self.window.main_GridLayout.addWidget(qcp,self.position,1)
        self.window.main_GridLayout.addWidget(btn,self.position,2)
        self.position = self.position + 1
        print("finish")
        btn.clicked.connect(lambda:self.del_todo(chkbtn,qcp,btn))
        chkbtn.clicked.connect(lambda:self.change_todo(chkbtn,qcp,btn))

    def finish_todo(self,text,date):
        self.current = QDate.currentDate()
        self.dday = QDate.fromString(date, "yyyy-MM-dd")
        self.interval = self.current.daysTo(self.dday)
        self.progressbarValue = 100-self.interval
        chkbtn = QPushButton(text, self)
        qcp = QProgressBar(self)
        btn = QPushButton("Del..",self)
        qcp.setValue(self.progressbarValue)
        qcp.setFormat(str(self.interval) + "-DAY")
        if (self.interval <= 5):                #d-day(interval)이 5일 이내라면 붉은색으로
            qcp.setStyleSheet("QProgressBar::chunk {background-color : red;}") # stylesheet 바꿔준다.
        self.window.finish_GridLayout.addWidget(chkbtn,self.finish_position,0)
        self.window.finish_GridLayout.addWidget(qcp,self.finish_position,1)
        self.window.finish_GridLayout.addWidget(btn,self.finish_position,2)
        self.finish_position = self.finish_position + 1
        print("finish_todo")
        btn.clicked.connect(lambda:self.del_done(chkbtn,qcp,btn))
        chkbtn.clicked.connect(lambda:self.toMain_todo(chkbtn,qcp,btn))

    def updateUI_finish(self):
        for self.i in reversed(range(self.window.finish_GridLayout.count())): 
            self.window.finish_GridLayout.itemAt(self.i).widget().setParent(None)

        self.cur.execute("SELECT * FROM todo;")
        self.rows = self.cur.fetchall()
        for self.row in self.rows:
            if self.row[2] == "0":
                self.finish_todo(self.row[0], self.row[1])
                print("updateUI_finish" + self.row[0])


    def updateUI_main(self):    
        for self.i in reversed(range(self.window.main_GridLayout.count())): 
            self.window.main_GridLayout.itemAt(self.i).widget().setParent(None)

        self.cur.execute("SELECT * FROM todo;")
        self.rows = self.cur.fetchall()
        for self.row in self.rows:
            if self.row[2] == "1":
                self.add_todo(self.row[0], self.row[1])
                print("updateUI_todo" + self.row[0])

    def del_todo(self, chkBox, qcp, btn):
        self.cur.execute("SELECT * FROM todo;")
        self.rows = self.cur.fetchall()
        for self.row in self.rows:
            self.cur.execute("DELETE FROM todo WHERE title = '" + chkBox.text()+ "'")
        self.conn.commit()
        print("del_commit")
        
        for self.row in self.rows:
            print(self.row)

        chkBox.deleteLater()
        qcp.deleteLater()
        btn.deleteLater()
        self.position = self.position - 1
        print(chkBox.text())
        
    
    def del_done(self, chkBox, qcp, btn):
        self.cur.execute("SELECT * FROM todo;")
        self.rows = self.cur.fetchall()
        for self.row in self.rows:
            self.cur.execute("DELETE FROM todo WHERE title = '" + chkBox.text()+ "'")
        self.conn.commit()
        print("del_commit")

        chkBox.deleteLater()
        qcp.deleteLater()
        btn.deleteLater()
        self.finish_position = self.finish_position - 1
        print(chkBox.text())
        

    def change_todo(self,chkBox,qcp,btn):
        self.cur.execute("SELECT * FROM todo;")
        self.rows = self.cur.fetchall()
        for self.row in self.rows:
            self.cur.execute("UPDATE todo SET flag = '0' WHERE title = '" + chkBox.text()+ "'")
        self.conn.commit()
        for self.row in self.rows:
            print(self.row)

        chkBox.deleteLater()
        qcp.deleteLater()
        btn.deleteLater()
        self.position = self.position - 1
        
        
    def toMain_todo(self,chkBox,qcp,btn):
        self.cur.execute("SELECT * FROM todo;")
        self.rows = self.cur.fetchall()
        for self.row in self.rows:
            self.cur.execute("UPDATE todo SET flag = '1' WHERE title = '" + chkBox.text()+ "'")
        self.conn.commit()    

        chkBox.deleteLater()
        qcp.deleteLater()
        btn.deleteLater()
        self.finish_position = self.finish_position - 1
        

class AddTodo:

    def __init__(self,ui):
        self.window = ui
        self.currentAdd = QDate.currentDate()
        self.window.add_currentDate.setText("Today : {0}".format(self.currentAdd.toString(Qt.DefaultLocaleLongDate)))
        self.status = '1'
        self.window.add_Calender.clicked.connect(self.setDate)          #달력 선택되었을때 시그널
        self.window.add_Calender.selectionChanged.connect(self.setDate) #다른 날짜 선택되었을때 시그널
        self.window.date_save.clicked.connect(self.saveTodo)
    def setDate(self): #선택 바뀔 때마다 setText해준다.
        self.TodoDate = self.window.add_Calender.selectedDate()
        self.window.text_date.setText("{0}".format(self.TodoDate.toString(Qt.DefaultLocaleLongDate)))
    
    def saveTodo(self):
        self.todo = self.window.text_subject.text()
        self.conn = sqlite3.connect("mydb.db")
        self.cur = self.conn.cursor()
        self.cur.execute("INSERT INTO todo VALUES('"+ self.todo +"', '" + self.TodoDate.toString(Qt.ISODate) + "', '" + self.status + "');")
        self.conn.commit()
        for self.i in reversed(range(self.window.main_GridLayout.count())): 
            self.window.main_GridLayout.itemAt(self.i).widget().setParent(None)
        print("deleteAll")

        self.cur.execute("SELECT * FROM todo;")
        self.rows = self.cur.fetchall()
        for self.row in self.rows:
            if self.row[2] == "1":
                todoList.add_todo(self.row[0], self.row[1])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)                  #기본설정
    Form = QtWidgets.QMainWindow()        #main_win                       #기본설정
    ui = MainTodo_ver1.Ui_MainWindow()                      #MainTodo의 ui_MainWindow ( ui_form class을 ui에 담는다)
    ui.setupUi(Form)
    todoList = TodoList(ui) 
    loginPage = login_Page(ui)
    stackPage = stack_Page(ui)
    addTodo = AddTodo(ui)
    #update = Update(ui)
    Form.show()
    sys.exit(app.exec_())

