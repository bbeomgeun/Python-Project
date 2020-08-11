import sqlite3
import time

conn = sqlite3.connect("mydb.db")
cur = conn.cursor()
cur.execute("DELETE FROM todo WHERE flag='1'")
conn.commit()
#cur.execute("INSERT INTO todo VALUES('스터디과제', '2020-07-29', '1');")
#cur.execute("INSERT INTO user VALUES('igrus', '1234');")
#cur.execute("DROP TABLE info")
#cur.execute("CREATE TABLE todo (title TEXT, date TEXT, flag TEXT);")
# cur.execute("CREATE TABLE user (id TEXT, pw TEXT);")
# cur.execute("CREATE TABLE info (id TEXT, age INT, gender TEXT, number INT);")

# cur.execute("INSERT INTO user VALUES('igrus', '1234');")
# cur.execute("INSERT INTO info VALUES('igrus', '24', 'man', '01071858942');")
# cur.execute("INSERT INTO user VALUES('miki308', '12345');")
# cur.execute("INSERT INTO user VALUES('nyanya', '123');")

# print("--------------------------------")
# print("-TodoList에 오신 것을 환영합니다-")
# print("--------------------------------\n")
# errorCount = 0
# while(1):
#     conn = sqlite3.connect("mydb.db")
#     cur = conn.cursor()
#     result = 0
#     askNumber = 0
#     number = int(input("\n1. 로그인 2. 회원가입 3. 나가기 : "))
#     if (number == 1):
#         print("************")
#         id = input("ID : ")
#         pw = input("PW : ")
#         print("************")
#         cur.execute("SELECT * FROM user;")
#         rows = cur.fetchall()
#         for row in rows:
#             if id == row[0]:
#                 result = 1
#                 if pw == row[1]:
#                     result = 2
#                     break
#         if result == 0:
#             print("\n***경고***")
#             print("아이디가 존재하지 않습니다!")
#             print("회원가입을 하시겠습니까?")
#             askNumber = int(input("1. yes 2. no")) ## 수정사항 yes를 누르면 회원가입으로 안들어가짐
#         elif result == 1:
#             print("\n***경고***")
#             print("비밀번호가 일치하지 않습니다!")
#             errorCount += 1
#             if errorCount < 5:
#                 print("\n로그인" +str(errorCount)+"회 오류")
#                 print("5회 이상 오류시 프로그램이 종료됩니다.\n")
#             elif errorCount == 5:
#                 print("5회 이상 오류로 프로그램이 종료됩니다.")
#                 break
#         elif result == 2:
#             print("로그인이 되었습니다!")
#             print("프로그램에 입장됩니다!")
#             for i in range(0,3):
#                 print("Loading~~")
#                 time.sleep(1)
#             break
#     elif (number == 2 or askNumber == 1):
#         print("**회원가입 페이지에 오신 것을 환영합니다**")
#         print("정보를 입력해주세요.")
#         print("----------------------\n")
#         while(1):
#             infoResult = 0
#             id = input("ID : ")
#             cur.execute("SELECT * FROM user;")
#             rows = cur.fetchall()
#             for row in rows:
#                 if id == row[0]:
#                     infoResult = 1
#             if infoResult == 1:
#                 print("이미 등록된 ID입니다.\n다시 입력해주세요.\n")
#             elif infoResult == 0:
#                 print("사용가능한 ID입니다.")
#                 ok = int(input("사용하시겠습니까? 1. Yes 2. No : "))
#                 if ok == 1:
#                     break
#                 elif ok == 1:
#                     continue
#         print("----------------------\n")       
#         while(1):
#             pw = input("PW : ")
#             if len(pw)<8:
#                 print("8글자 이상 비밀번호를 설정해주세요.")
#             else:
#                 break
#         print("----------------------\n")
#         print("나이를 입력해주세요.")
#         age = int(input("나이 : "))
#         print("----------------------\n")
#         print("성별을 입력해주세요.")
#         Gender = ""
#         gender = int(input("1. man 2. woman : "))
#         if gender == 1:
#             Gender = "man"
#         elif gender == 2:
#             Gender = "woman"
#         print("----------------------\n")
#         print("전화번호를 입력해주세요.")
#         phoneNumber = int(input("전화번호 : "))
#         print("----------------------\n")
#         cur.execute("INSERT INTO info VALUES(' "+ id+" ' , "+" '"+str(age)+"',"+"'"+Gender+"',"+"'"+str(phoneNumber)+"');")
#         cur.execute("INSERT INTO user VALUES('" + id + "'," + "'" + pw + "');") 
            # "INSERT INTO table VALUES(' + x + " ', " + "'" + y + "');")
#         print("회원가입이 완료되었습니다!")
#         #cur.execute("INSERT INTO info VALUES('igrus', '24', 'man', '01071858942');")
#         conn.commit() # 데이터베이스 값을 수정하겠다. 승인
        
#     elif(number == 3):
#         print("프로그램을 종료합니다.")
#         conn.close()
#         break