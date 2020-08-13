# 1. 입출력과 if문을 이용해서 시뮬레이션 게임 만들기
# 조건은 2개입니다.
# 첫 번째. 5시간 이상 투자할 것
# 두 번째. 첫 시작 if문은 3단계 깊이까지 들어가도록 할 것
print("시뮬레이션 게임")
print("음식주문시스템. (잔액 5천원)")
money = 5000
num = int(input("1. 샌드위치 2. 안먹을래요."))
if (num == 1):
    num1 = int(input("1. 서브웨이 __ 2. 이삭토스트 __ 3.에그드랍"))
    if(num1 == 1):
        # while(){
        num2 = int(input("어떤 메뉴를 드시겠습니까? \n 1. 터키(4800원) 2. 에그마요(5500원) 3. 스테이크&치즈(5000원"))
        if(num2==1):
            print("터키를 주문하셨습니다. 가격은 4800원입니다. 음료 필요하세요?")
            money -= 4800
            num3 = int(input("1.yes 2. no"))
            if(num3 == 1):
                num4 = int(input("어떤 음료 주문하시겠어요? \n 1.콜라 2. 사이다"))
                if(num4 == 1):
                    print("콜라 주문하셨습니다. 500원입니다. 주문완료입니다.")
                    money -= 500
                    print("남은잔액 : ", money)
                elif(num4 == 2):
                    print("사이다 주문하셨습니다. 500원입니다. 주문완료입니다.")
                    money -= 500
                    print("남은잔액 : ", money)
            elif(num3 == 2):
                print("주문 완료되었습니다.")
        elif(num2==2):
            print("에그마요를 주문하셨습니다. 가격은 5500원입니다. 음료 필요하세요?")
            money -= 5500
            num3 = int(input("1.yes 2. no"))
            if(num3 == 1):
                num4 = int(input("어떤 음료 주문하시겠어요? \n 1.콜라 2. 사이다"))
                if(num4 == 1):
                    print("콜라 주문하셨습니다. 500원입니다. 주문완료입니다.")
                    money -= 500
                    print("남은잔액 : ", money)
                elif(num4 == 2):
                    print("사이다 주문하셨습니다. 500원입니다. 주문완료입니다.")
                    money -= 500
                    print("남은잔액 : ", money)
            elif(num3 == 2):
                print("주문 완료되었습니다.")
        elif(num2==3):
            print("스테이크&치즈를 주문하셨습니다. 가격은 5000원입니다. 음료 필요하세요?")
            money -= 5000
            num3 = int(input("1.yes 2. no"))
            if(num3 == 1):
                num4 = int(input("어떤 음료 주문하시겠어요? \n 1.콜라 2. 사이다"))
                if(num4 == 1):
                    print("콜라 주문하셨습니다. 500원입니다. 주문완료입니다.")
                    money -= 500
                    print("남은잔액 : ", money)
                elif(num4 == 2):
                    print("사이다 주문하셨습니다. 500원입니다. 주문완료입니다.")
                    money -= 500
                    print("남은잔액 : ", money)
            elif(num3 == 2):
                print("주문 완료되었습니다.") 
    elif(num1==2):
        num2 = int(input("어떤 메뉴를 드시겠습니까? \n 1. 햄토스트(2500) 2. 치즈토스트(2000원) 3. 프리미엄토스트(3500원"))
        if(num2==1):
            print("햄토스트를 주문하셨습니다. 가격은 2500원입니다. 음료 필요하세요?")
            money -= 2500
            num3 = int(input("1.yes 2. no"))
            if(num3 == 1):
                num4 = int(input("어떤 음료 주문하시겠어요? \n 1.오렌지주스 2. 사이다"))
                if(num4 == 1):
                    print("오렌지주스 주문하셨습니다. 500원입니다. 주문완료입니다.")
                    money -= 500
                    print("남은잔액 : ", money)
                elif(num4 == 2):
                    print("사이다 주문하셨습니다. 500원입니다. 주문완료입니다.")
                    money -= 500
                    print("남은잔액 : ", money)
            elif(num3 == 2):
                print("주문 완료되었습니다.")
        elif(num2==2):
            print("치즈토스트를 주문하셨습니다. 가격은 2000원입니다. 음료 필요하세요?")
            money -= 2000
            num3 = int(input("1.yes 2. no"))
            if(num3 == 1):
                num4 = int(input("어떤 음료 주문하시겠어요? \n 1.오렌지쥬스 2. 사이다"))
                if(num4 == 1):
                    print("오렌지쥬스 주문하셨습니다. 500원입니다. 주문완료입니다.")
                    money -= 500
                    print("남은잔액 : ", money)
                elif(num4 == 2):
                    print("사이다 주문하셨습니다. 500원입니다. 주문완료입니다.")
                    money -= 500
                    print("남은잔액 : ", money)
            elif(num3 ==2):
                print("주문 완료되었습니다.")
        elif(num2==3):
            print("프리미엄토스트를 주문하셨습니다. 가격은 3500원입니다. 음료 필요하세요?")
            money -= 3500
            num3 = int(input("1.yes 2. no"))
            if(num3 == 1):
                num4 = int(input("어떤 음료 주문하시겠어요? \n 1.오렌지쥬스 2. 사이다"))
                if(num4 == 1):
                    print("오렌지쥬스 주문하셨습니다. 500원입니다. 주문완료입니다.")
                    money -= 500
                    print("남은잔액 : ", money)
                elif(num4 == 2):
                    print("사이다 주문하셨습니다. 500원입니다. 주문완료입니다.")
                    money -= 500
                    print("남은잔액 : ", money)
            elif(num3 ==2):
                print("주문 완료되었습니다.")
    elif(num1==3):
        num2 = int(input("어떤 메뉴를 드시겠습니까? \n 1.베이컨더블치즈(4500원) 2. 갈릭베이컨치즈(4000원) 3. 닭가슴살치즈(3500원"))
        if(num2==1):
            print("베이컨더블치즈를 주문하셨습니다. 가격은 4500원입니다. 음료 필요하세요?")
            money -= 4500
            num3 = int(input("1.yes 2. no"))
            if(num3 == 1):
                num4 = int(input("어떤 음료 주문하시겠어요? \n 1.아메리카노 2. 우유"))
                if(num4 == 1):
                    print("아메리카노 주문하셨습니다. 500원입니다. 주문완료입니다.")
                    money -= 500
                    print("남은잔액 : ", money)
                elif(num4 == 2):
                    print("우유 주문하셨습니다. 500원입니다. 주문완료입니다.")
                    money -= 500
                    print("남은잔액 : ", money)
            elif(num3 ==2):
                print("주문 완료되었습니다.")
        elif(num2==2):
            print("갈릭베이컨치즈를 주문하셨습니다. 가격은 4000원입니다. 음료 필요하세요?")
            money -= 4000
            num3 = int(input("1.yes 2. no"))
            if(num3 == 1):
                num4 = int(input("어떤 음료 주문하시겠어요? \n 1.아메리카노 2. 우유"))
                if(num4 == 1):
                    print("아메리카노 주문하셨습니다. 500원입니다. 주문완료입니다.")
                    money -= 500
                    print("남은잔액 : ", money)
                elif(num4 == 2):
                    print("우유 주문하셨습니다. 500원입니다. 주문완료입니다.")
                    money -= 500
                    print("남은잔액 : ", money)
            elif(num3 == 2):
                print("주문 완료되었습니다.")
        elif(num2==3):
            print("프리미엄토스트를 주문하셨습니다. 가격은 3500원입니다. 음료 필요하세요?")
            money -= 3500
            num3 = int(input("1.yes 2. no"))
            if(num3 == 1):
                num4 = int(input("어떤 음료 주문하시겠어요? \n 1.아메리카노 2. 우유"))
                if(num4 == 1):
                    print("아메리카노 주문하셨습니다. 500원입니다. 주문완료입니다.")
                    money -= 500
                    print("남은잔액 : ", money)
                elif(num4 == 2):
                    print("우유 주문하셨습니다. 500원입니다. 주문완료입니다.")
                    money -= 500
                    print("남은잔액 : ", money)
            elif(num3 == 2):
                print("주문 완료되었습니다.") 
elif (num == 2):
    print("종료합니다.")    
    

# 2. 스도쿠 만들기
# 가로와 세로에만 중복되는 숫자가 없는 스도쿠를 출력하면됩니다.
# N을 입력받으면 N x N 의 스도쿠가 출력되게 하면됩니다.

# Ex) 입력은 4
# 1 3 2 4
# 2 1 4 3
# 3 4 1 2 
# 4 2 3 1

# n = int(input("숫자를 입력하세요 : "))
# list = []
# for i in range(1,n+1):
#     list.append(i)

# for j in range(0,n):
#     count = 0
#     for k in range(j,n):
#         print(list[k],",", end = "")
#         count += 1
#         if(k==n and count != n):
#             k=0
#             if(count == n):
#                 break
#             print("\n")

# from random import *

# n = int(input("숫자를 입력하세요 : "))
# sudoku = [[0]*n for i in range(n)]

# for i in range(n):
#     for j in range(n):
#         # number = randint(1,n)
#         while():  #new 값이 나올때까지 돌린다.
#             number = randint(1,n)
#             for width in range(0,j): #i고정 0~j-1탐색(가로)
#                 if(number != sudoku[i][width]): #없으면
#                     # for height in range(0,i):
#                     #     if(number != sudoku[height][j]):
#                     sudoku[i][j] = number
#             if (j == n-1):
#                 break
#         print(sudoku[i][j], end = ' ')
#     print('\n')

from random import *
n = int(input("숫자를 입력하세요 : "))
sudoku = [[0]*n for i in range(n)]

count = 0
for i in range(n):
    check = []
    for j in range(n):
        while(1):
            number = randint(1,n)
            if number not in check:
                sudoku[i][j] = number
                check.append(number)
                count += 1
                break
            # elif number in check:
            #     continue
        print(sudoku[i][j], end = ' ')
    print('\n')
            