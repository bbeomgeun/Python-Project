# 1. 스탑워치
# (첫 쓰레드 : 시간흐름 - 무한정 시간을 돌리는 것
# (두번째 쓰레드 : 시간 정지 기록 - 무한정 버튼이 눌리는지 체크 -> 눌리면 첫쓰레드가서 시간을 출력)

import time
import threading #쓰레드 모듈

class Record(threading.Thread): #시간을 기록하는 쓰레드
    def __init__(self):
        threading.Thread.__init__(self) #기본문법

    def run(self):
        while True:
            input("아무 입력 : ") 
            print(exTime.t/10) #(Timer의 변수로 전역변수로 접근가능)

class Timer(threading.Thread): #시간이 돌아가는 쓰레드
    def __init__(self): #생성자
        threading.Thread.__init__(self) # 상속 - Threading 모듈에서 가져올 때 상속받은 클래스의 생성자를 실행하겠다.
        self.t = 0 

    def run(self): # run으로 하자
        while True: #무한루프로 쓰레드가 돌아가는것은 프로그램 끝날때까지 계속 돌아감 - 메모리누수
            # print(self.t/10)
            self.t += 1
            time.sleep(0.1)
            if self.t >100: #조건문으로 제어를 하자 10s
                break

if __name__ == "__main__" : 
    exTime = Timer()  # 메인에 선언한 변수 : 전역변수처럼 사용가능
    exTime.start() # .start() 쓰레드시작

    exRecord = Record() # 클래스 선언
    exRecord.start()

# 2. 버블소트 100 리스트 X 10개 - 병렬처리(10개의 쓰레드 한꺼번에 돌리기)

# import time
# import threading #쓰레드 모듈
# import random

# class Sort(threading.Thread): #시간을 기록하는 쓰레드
#     def __init__(self, exList):
#         self.list = exList
#         threading.Thread.__init__(self) #기본문법

#     def run(self):
#         for a in range(0,100): # 버블 정렬
#             for b in range(a,100):
#                 if exList[a] > exList[b]:
#                     swap = exList[a]
#                     exList[a] = exList[b]
#                     exList[b] = swap

#             for a in range(0,100):
#                 print(exList[a])

# if __name__ == "__main__" : 

#     exList = []

#     for a in range(0,10):
#         tmpList = []
#         for b in range(0,100):
#             num = random.randint(0,1000)
#             tmpList.append(num)
#         exList.append(tmpList)

#         for a in range(0,10):
#             s = Sort(exList[a]) # 쓰레드 for문으로 10개 선언(sort를 각자 열로 돌린다(100개짜리 list 1줄))
#             s.start()
