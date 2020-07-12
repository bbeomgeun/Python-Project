#이 곳이 메인 -> 여기에서 interface를 불러온다. ( interface에도 main 이 있을 수 있다.)
#main함수 - 이곳에서 프로그램의 시작이 된다.
# GUIClass에서 main을 만들고 다른 클래스들을 호출하면 guiclass에서 시작된다.
# 고친 틀을 먼저 실행시키고 싶다. 부분적으로 확인할때 main함수를 파일 별로 만들어서 실행시킬 수 있다.

from PyQt5 import QtCore, QtGui, QtWidgets
import interface
import time
import threading

#현재상황 : clicked.connect(self.begin)으로 진행했더니 버튼클릭할때마다 상태를 바꿔서 숫자를 멈추고 다시 돌려야하는데
#쓰레딩을 어떻게 시작해야할지 모르겠음. 쓰레딩.start를 두번 이상 하면 안된다.

class GUIClass(threading.Thread):
#### method
    def __init__(self, ui):
        threading.Thread.__init__(self)
        self.window = ui                                    # window 변수에 ui
        self.number = 0                                     # 출력할 number 변수
        self.status = 0
        self.start()
        self.status = 0
        self.window.pushbtn.clicked.connect(self.onOff)     #window(ui)에 있는 버튼위젯 눌리면 begin메소드 연결
        
#### slot - pyQt에서의 버튼리스너
    def run(self):                                         # 쓰레딩 시작되면 
          while(True):
            if self.status == 1:                                  #1초에 숫자 1개씩 늘어나고 ui에 있는 label에 settext(숫자)
                self.number += 1
                self.window.label.setText(str(self.number))
                time.sleep(1)
            elif self.status == 0:
                self.window.label.setText(str(self.number))
    
    def begin(self):                                        # 쓰레딩 시작용 메소드
       self.start()                                         #객체.start() -> 자기자신 self.start()

    def onOff(self):
        if(self.status == 0):
            self.status = 1
        elif(self.status == 1):
            self.status = 0

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)                  #기본설정
    Form = QtWidgets.QWidget()                              #기본설정
    ui = interface.Ui_Form()                                #interface의 ui_form class ( ui_form class을 ui에 담는다)
    ui.setupUi(Form)
    gc = GUIClass(ui)                                       #GUIClass 객체 생성(파라미터 ui)
    Form.show()
    sys.exit(app.exec_())

    
    ##스탑워치 정지하는거(다시 누르면 시작, 정지   누를대마다 상태 바꾸고 조건문으로 하기) + pyqt로 디자인 만들어오기(화면구성)