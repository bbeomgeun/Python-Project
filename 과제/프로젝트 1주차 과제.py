# 예외처리버전
# print("시뮬레이션 게임")
# num = int(input("1. 먹어요 2. 안먹어요"))
# money = 5000
# if(num==1):
#     num1 = int(input("1. 맘스터치 2. kfc"))
#     if(num1 == 1):
#         while(1):
#             num2 = int(input("1. 싸이버거 2. 싸이버거세트"))
#             if (num2 == 1):
#                 print("싸이버거를 주문하셨습니다.")
#                 money -= 5000
#                 if(money <0):
#                     print("금액이 부족합니다.")
#                 else:
#                     print("정상주문되었습니다.")
#                     break
#                 break
#             if(num2 == 2):
#                 print("싸이버거 세트를 주문하셨습니다.")
#                 money -= 5500
#                 if(money <0):
#                     print("금액이 부족합니다.")
#                 else:
#                     print("정상주문되었습니다.")
#                     break
#                 break

import random

def makeSudoku():
    sudoku = [[0 for col in range(9)] for row in range(9)]

    for row in range(9):
        for col in range(9):
            number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

            if row == 0 and col == 0:
                random.shuffle(number)
                sudoku[0][0] = number.pop()
            elif row == 0:
                for check_col in range(col):
                    if sudoku[0][check_col] in number:
                        number.remove(sudoku[0][check_col])
                random.shuffle(number)
                sudoku[0][col] = number.pop()
            elif col == 0:
                for check_row in range(row):
                    if sudoku[check_row][0] in number:
                        number.remove(sudoku[check_row][0])
                random.shuffle(number)
                sudoku[row][0] = number.pop()
            else:
                for check_row in range(row):
                    if sudoku[check_row][col] in number:
                        number.remove(sudoku[check_row][col])
                for check_col in range(col):
                    if sudoku[row][check_col] in number:
                        number.remove(sudoku[row][check_col])
                random.shuffle(number)
                sudoku[row][col] = number.pop()

    for row in range(9):
        print(sudoku[row][:], sep="\n")

makeSudoku()