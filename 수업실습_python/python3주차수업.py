# def calAvg(num1, num2, num3, num4): #함수
#     sum = num1+ num2 + num3 + num4
#     average = sum/4
#     print(average)

# if __name__ == "__main__" : #메인함수
#     student1 = [100,80,70,10]
#     student2 = [50,60,80,100]
#     student3 = [90,100,95,100]

#     calAvg(student1[0] , student1[1], student1[2] , student1[3])

#     calAvg(student2[0] , student2[1] , student2[2] , student2[3])

#     calAvg(student3[0] , student3[1] , student3[2] , student3[3])

class character: #객체
    def __init__(self, nickname, level): #생성자
        self.name  = nickname #클래스 안의 name변수 생성 후 변수받기
        self.level = level

    def moveRight(self): #self를 넣어줘야한다.
        print(self.name+ "는 오른쪽으로 이동")
    def moveLeft(self):
        print(self.name + "는 왼쪽으로 이동")
    def Jump(self):
        print(self.name + " 점프!")
    def attack(self):
        print(self.name + " 공격!")

    def info(self):
        print("닉네임 : " + self.name)
        print("레벨 : " + str(self.level))
    
    def setLevel(self, afterlevel):
        self.level = afterlevel

a = character("A", 1) #객체선언
b = character("B", 200)

a.info()
a.setLevel(20)
a.info()
