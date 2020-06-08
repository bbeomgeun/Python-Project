# 200520 python study #1

# tip : 구글링 +aa -bb (a는 무조건 포함, b는 빼주세요).

# 파이썬 인터프리터 언어(한줄씩 읽어서 오류 어느적 허용이지만 느리다 -> 대규모프로젝트는 못함) / 객체지향 / 크로스템플릿
#  - PyQt GUI프레임워크 : 빠르고 효율좋음 (해커톤에 어울린다)

# C 컴파일(빠르지만 전체적으로 오류가 없어야함) / 절차지향



# tmp = input()
# print(tmp) 입출력


# tmp = []

# tmp.append(1)
# tmp.append(2)
# tmp.append(3)

# print(tmp) 배열/리스트

# for i in range(0, 3):
#     print(tmp[i]) for문

# for i in tmp:
#     print(i) for문을 통해 list에 바로 접근

# var1 = int(input("첫 번째 값을 입력하세요."))
# var2 = int(input("두 번째 값을 입력하세요."))
#input은 string으로 입력되므로 int를 붙여준다.
# print(var1 + var2)
# print(var1-var2)
# print(var1*var2)
# print(var1/var2)
# print(var1%var2)

# print(var1**var2)
# print(var1//var2) 몫

# if var1>var2 :
#     print("var1이 더 크다.")
# elif var1<=var2:
#     print("var2가 크거나 같다.")
# else:
#     print("둘다 해당되지 않음.")

# a = 0

# while a <3:
#     a+=1
#     print(a)

#학점계산기
# list = []
# sum = 0
# n = int(input("과목 갯수를 입력하세요 : "))

# for i in range(0,n):
#     grade = input("학점 입력 : ")
#     if grade == "A+":
#         list.append(4.5)
#     elif grade == "A0":
#         list.append(4.0)
#     elif grade == "B+":
#         list.append(3.5)
#     elif grade == "B0":
#         list.append(3.0)
#     elif grade == "C+":
#         list.append(2.5)
#     elif grade == "C0":
#         list.append(2.0)
#     elif grade == "D+":
#         list.append(1.5)
#     elif grade == "D0":
#         list.append(1.0)
#     else:
#         list.append(0)

# for k in list:
#     sum +=k

# print("학점 = ", sum/n)

# n = int(input())
# list = []
# listdown = []
# count = 0
# for i in range(0,n):
#     k = float(input())
#     list.append(k)

# for k in list:
#     if k <1.75:
#         listdown.append(k)
# listdown.sort()
# print("학고 수", len(listdown))
# print("학고학생의 최고평점", listdown[len(listdown)-1])


# list.sort()
# list.reverse() 
# count = n // 2

# print("장학생수", count)
# print("장학생의 최저평점", list[count-1])
