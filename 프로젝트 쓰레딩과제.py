# #경주게임만들기 ->각각의 말 속도가 달라야한다
    #threading 종료하기
    # 말속도가 변하게끔 해보자 -> 달리다가 지치거나, 갑자기 빠르게 달리거나 (랜덤을 계속 돌린다)
    # 반복문으로 곱하기를 줘도 점점 빨라진다.
    # 쓰레드를 할 때, 만약 5마리
    # 5개의 포켓몬 쓰레드 -> 출력 일절 관여 X, 자신의 데이터만 가지고 있어야 함. 
    # 1개의 출력전용 쓰레드가 필수
    # --> 출력전용에서 5개의 쓰레드를 선언, 접근을 해서 가져오는 것 뿐. 하지만 단지 위의 쓰레드에서 위치가 계속해서 바뀌는 것일뿐.

import time
import threading
import random
class Horses1(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.current = 0
        self.luckyNumberstart = 60
        self.luckyNumberend = 80
        self.randomNumber = 0
        self.onOff = 0
    def run(self):
        while(self.current != game.track):
            self.randomNumber = random.randint(1,100)
            if self.randomNumber>= 1 and self.randomNumber <= 40:
                self.current += 2                 # 그냥 걷기 +2 40퍼
            elif self.randomNumber >= 41 and self.randomNumber <= self.luckyNumberstart:
                self.current += 4                 # 뛰기 + 4 20퍼
            elif self.randomNumber > self.luckyNumberstart and self.randomNumber <= self.luckyNumberend:
                self.current += 15                 # 럭키점프 + 15 (강화시 이 확률이 높아짐) 20퍼
            elif self.randomNumber > self.luckyNumberend and self.randomNumber <=100:
                self.current -= 3                 # 넘어지기 20퍼
            if(self.current >= game.track):
                self.current = game.track
                self.onOff = 1
            if(addHorses1.onOff == 1 or addHorses2.onOff == 1 or addHorses3.onOff == 1 or addHorses4.onOff == 1):
                break
            time.sleep(1)
            

class Horses2(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.current = 0
        self.luckyNumberstart = 70
        self.luckyNumberend = 80
        self.randomNumber = 0
        self.onOff = 0
    def run(self):
        while(self.current != game.track):
            self.randomNumber = random.randint(1,100)
            if self.randomNumber>= 1 and self.randomNumber <= 50:
                self.current += 3                 # 그냥 걷기 +3 50퍼
            elif self.randomNumber >= 51 and self.randomNumber <= self.luckyNumberstart:
                self.current += 5                 # 뛰기 + 5 20퍼
            elif self.randomNumber > self.luckyNumberstart and self.randomNumber <= self.luckyNumberend:
                self.current += 10                 # 럭키점프 + 10 10퍼 (강화시 이 확률이 높아짐)
            elif self.randomNumber > self.luckyNumberend and self.randomNumber <=100:
                self.current -= 3                 # 넘어지기 -3 20퍼
            if(self.current >= game.track):
                self.current = game.track
                self.onOff = 1
            if(addHorses1.onOff == 1 or addHorses2.onOff == 1 or addHorses3.onOff == 1 or addHorses4.onOff == 1):
                break
            time.sleep(1)

class Horses3(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.current = 0
        self.luckyNumberstart = 60
        self.luckyNumberend = 70
        self.onOffskill = 0
        self.randomNumber = 0
        self.onOff = 0
    def run(self):
        while(self.current != game.track):
            self.randomNumber = random.randint(1,100)
            if self.randomNumber>= 1 and self.randomNumber <= 40:
                self.current += 2                 # 그냥 걷기 +1
            elif self.randomNumber >= 41 and self.randomNumber <= self.luckyNumberstart:
                self.current += 4                 # 뛰기 + 2
            elif self.randomNumber > self.luckyNumberstart and self.randomNumber <= self.luckyNumberend:
                self.current += 10                 # 럭키점프 + 4 (강화시 이 확률이 높아짐)
            elif self.randomNumber > self.luckyNumberend and self.randomNumber <=75:
                self.onOffskill = 1
            elif self.randomNumber > 76 and self.randomNumber <=100:
                if (self.onOffskill == 0):
                    self.current -= 3               # 넘어지기
                elif (self.onOffskill == 1):
                    self.current += 1
                #걷기(+2칸) 40% / 점프(+4칸) 20% / 럭키점프(+10칸) 10% / 우니! 5% /  미끄러지기(-3칸) 25%의 확률로 발동
            if(self.current >= game.track):
                self.current = game.track
                self.onOff = 1
            if(addHorses1.onOff == 1 or addHorses2.onOff == 1 or addHorses3.onOff == 1 or addHorses4.onOff == 1):
                break
            time.sleep(1)

class Horses4(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.current = 0
        self.luckyNumberstart = 60
        self.luckyNumberend = 70
        self.randomNumber = 0
        self.onOff = 0
    def run(self):
        while(self.current != game.track):
            self.randomNumber = random.randint(1,100)
            if self.randomNumber>= 1 and self.randomNumber <= 40:
                self.current += 5                 # 그냥 걷기 
            elif self.randomNumber >= 41 and self.randomNumber <= self.luckyNumberstart:
                self.current += 8                 # 뛰기 
            elif self.randomNumber > self.luckyNumberstart and self.randomNumber <= self.luckyNumberend:
                self.current += 10                 # 럭키점프  (강화시 이 확률이 높아짐)
            elif self.randomNumber > self.luckyNumberend and self.randomNumber <=100:
                self.current -= 6                 # 넘어지기
            if(self.current >= game.track):
                self.current = game.track
                self.onOff = 1
                #걷기(+5칸) 40% / 점프(+8칸) 20% / 럭키점프(+10칸) 10% / 미끄러지기(-6칸) 30%의 확률로 발동
            if(addHorses1.onOff == 1 or addHorses2.onOff == 1 or addHorses3.onOff == 1 or addHorses4.onOff == 1):
                break
            time.sleep(1)

class printHorse(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.track = 50
        self.result = 0
    def run(self):
        while (1): #addHorses1.onOff == 1 or addHorses2.onOff == 1 or addHorses3.onOff == 1 or addHorses4.onOff == 1 
            if(addHorses1.onOff == 1):
                print("경기 결과 : 다오가 이겼습니다!")
                self.result = 1
                break
            elif(addHorses2.onOff == 1):
                print("경기 결과 : 배찌가 이겼습니다!")
                self.result = 2
                break
            elif(addHorses3.onOff == 1):
                print("경기 결과 : 우니가 이겼습니다!")
                self.result = 3
                break
            elif(addHorses4.onOff == 1):
                print("경기 결과 : 디지니가 이겼습니다!")
                self.result = 4
                break
            print("-"*self.track)
            print(" " * addHorses1.current + "다오"+str(addHorses1.current))
            print(" " * addHorses2.current + "배찌"+str(addHorses2.current))
            print(" " * addHorses3.current + "우니"+str(addHorses3.current))
            print(" " * addHorses4.current + "디지니"+str(addHorses4.current))
            print("-"*self.track)
            time.sleep(1)    
            

if __name__ == "__main__" : 

    addHorses1 = Horses1()
    addHorses2 = Horses2()
    addHorses3 = Horses3()
    addHorses4 = Horses4()
    game = printHorse()

    print("카트 경마장에 오신 걸 환영합니다.\n")
    totalMoney = 1000
    askBetting = 0
    askMoney =0
    while(1):
        print("0. 말 설명 1. 베팅하기  2. 말 업그레이드 하기 3.게임 시작 4. 나가기\n")
        selectNumber = int(input("번호를 골라주세요 : "))
        if (selectNumber == 0):
            print("\n")
            print("------------------------------------------------------------------------------------------------------------------")
            print("-  다오 : 걷기(+2칸) 40% / 점프(+4칸) 20% / 럭키점프(+15칸) 20% / 미끄러지기(-3칸) 20%의 확률로 발동                ")
            print("- 특징 : 캐릭터들 중에서 럭키점프의 효과가 가장 크다! - 운을 시험해보자..\n")
            print("-  배찌 : 걷기(+3칸) 50% / 점프(+5칸) 20% / 럭키점프(+10칸) 10% / 미끄러지기(-3칸) 20%의 확률로 발동                ")
            print("- 특징 : 캐릭터들 중에서 걷기와 점프의 확률(총 70%)이 가장 크다! - 꾸준함을 원한다면..\n")
            print("-  우니 : 걷기(+2칸) 40% / 점프(+4칸) 20% / 럭키점프(+10칸) 10% / 우니! 5% /  미끄러지기(-3칸) 25%의 확률로 발동    ")
            print("- 특징 : 고유효과인 우니! 가 발동되면 절대 미끄러지지 않는다(발동효과 5%)                                           ")
            print("-    발동될시 미끄러지기의 확률 10%가 걷기확률에 더해진다! \n")
            print("- 디지니 : 걷기(+5칸) 40% / 점프(+8칸) 20% / 럭키점프(+10칸) 10% / 미끄러지기(-6칸) 30%의 확률로 발동          ")
            print("- 특징 : 기본적인 스펙은 가장 좋다! 하지만 넘어지면 크게 넘어진다!                                            ")
            print("------------------------------------------------------------------------------------------------------------------")
            print("\n")
        if (selectNumber == 1):
            askBetting = int(input("1. 다오    2. 배찌    3. 우니    4. 디지니 \n 어떤 캐릭터에 베팅하시겠습니까? : "))
            print("\n")
            while(1):
                askMoney = int(input("총 금액 : "+str(totalMoney)+"원 / 베팅과 업그레이드에 사용 가능 \n얼마를 베팅하시겠습니까? : ")) 
                print("\n")
                if (askMoney > totalMoney):
                    print("금액을 초과하셨습니다! ")
                    print("\n")
                    continue
                else:
                    print(str(askMoney)+"원을 베팅하셨습니다.\n")
                    print("*****우승시 5배!*****\n")
                    totalMoney = totalMoney - askMoney
                    break
        if (selectNumber == 2):
            while(1):
                print("\n---------------------------------------------------")
                print("*****1회 당 100원*****")
                print("업그레이드시 럭키점프의 확률이 올라갑니다!(럭키점프 확률 +2%, 점프 확률 -2%)\n")
                print("1. 다오    2. 배찌    3. 우니    4. 디지니 5. 나가기\n")
                upgradeNumber = int(input("어떤 캐릭터를 업그레이드 하시겠습니까?? : "))
                if (upgradeNumber == 1):
                    print("업그레이드 전 다오의 럭키점프 확률 : " + str(addHorses1.luckyNumberend - addHorses1.luckyNumberstart)+"%")
                    addHorses1.luckyNumberstart -= 2 # 2%올라감
                    print("업그레이드 후 다오의 럭키점프 확률 : " + str(addHorses1.luckyNumberend - addHorses1.luckyNumberstart)+"%")
                    totalMoney = totalMoney - 100
                    print("남은 금액 : " + str(totalMoney))

                elif (upgradeNumber == 2):
                    print("업그레이드 전 배찌의 럭키점프 확률 : " + str(addHorses2.luckyNumberend - addHorses2.luckyNumberstart)+"%")
                    addHorses2.luckyNumberstart -= 2 # 2%올라감
                    print("업그레이드 후 배찌의 럭키점프 확률 : " + str(addHorses2.luckyNumberend - addHorses2.luckyNumberstart)+"%")
                    totalMoney = totalMoney - 100
                    print("남은 금액 : " + str(totalMoney))

                elif (upgradeNumber == 3):
                    print("업그레이드 전 우니의 럭키점프 확률 : " + str(addHorses3.luckyNumberend - addHorses3.luckyNumberstart)+"%")
                    addHorses3.luckyNumberstart -= 2 # 2%올라감
                    print("업그레이드 후 우니의 럭키점프 확률 : " + str(addHorses3.luckyNumberend - addHorses3.luckyNumberstart)+"%")
                    totalMoney = totalMoney - 100
                    print("남은 금액 : " + str(totalMoney))

                elif (upgradeNumber == 4):
                    print("업그레이드 전 디지니의 럭키점프 확률 : " + str(addHorses4.luckyNumberend - addHorses4.luckyNumberstart)+"%")
                    addHorses4.luckyNumberstart -= 2 # 2%올라감
                    print("업그레이드 후 디지니의 럭키점프 확률 : " + str(addHorses4.luckyNumberend - addHorses4.luckyNumberstart)+"%")
                    totalMoney = totalMoney - 100
                    print("남은 금액 : " + str(totalMoney))
                elif (upgradeNumber == 5):
                    break
                else:
                    print("다시 입력해주세요!!")

        if (selectNumber == 3):  #쓰레드 시작  
            print("***경주가 시작되겠습니다!***")
            print("***        Start!!      ***")
            addHorses1.start()
            addHorses2.start()
            addHorses3.start()
            addHorses4.start()
            game.start()
            while(1):
                if(game.result != 0):
                    if(game.result == askBetting):
                        askMoney *= 5
                        totalMoney += askMoney
                        print("*** 배팅 당첨!!! 베팅금액의 5배!!! ***")
                        print("현재 금액 : " + str(totalMoney)+ "!!\n")
                        break
                    elif(game.result != askBetting):
                        print("*** 배팅 실패 ㅜ_ㅜ ***")
                        print("현재 금액 : " + str(totalMoney)+ "!!\n")
                        break
                
        if(selectNumber == 4):
            print("게임이 종료됩니다 \n다음에 또 이용해 주세요!\n")
            print("최종결과금액 : " + str(totalMoney))
            if(totalMoney >= 1000):
                print(str(totalMoney - 1000)+"원 얻고 갑니다!! ^0^")
            else:
                print(str(1000-totalMoney)+"원 잃고 갑니다.. ㅜ_ㅜ")
            break

        ##각 캐릭터 상태창이랑 트랙길이