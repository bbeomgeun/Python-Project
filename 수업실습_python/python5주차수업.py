# 20200701 데이터베이스 실습
# DB 생성
#anaconda prompt -> cd로 경로 설정 -> sqlite3 -> .open 이름.db(있으면 오픈, 없으면 생성)

import sqlite3
conn = sqlite3.connect("mydb.db")
cur = conn.cursor()

#테이블 만든다.
# cur.execute("CREATE TABLE user (id TEXT, pw TEXT);")
# cur.execute("CREATE TABLE info (id TEXT, age INT, gender TEXT, number INT);")
# 한번 만들면 끝 / 원래는 db코드 따로 보관


#눈으로 확인해보기 - SQLITE 확장 -> F1에 sqlite검색 -> 나의 db 선택 후 탐색기에 확인해보면 SQLITE EXPLORER가 보인다.

#데이터 넣기.
cur.execute("INSERT INTO user VALUES('igrus', '1234');")
cur.execute("INSERT INTO info VALUES('igrus', '24', 'man', '01071858942');")
cur.execute("INSERT INTO user VALUES('miki308', '12345');")
cur.execute("INSERT INTO user VALUES('nyanya', '123');")

# #데이터 가져오기
# cur.execute("SELECT * FROM user;")

# for row in cur.fetchall():
#     print(row) # ranged for / list형태로 가져온다.

#데이터 수정하기

# 로그인 만들기
# id = input("아이디를 입력하세요 : ")
# pw = input("비밀번호를 입력하세요 : ")

# #있는 값인지 비교
# cur.execute("SELECT * FROM user;")
# for row in cur.fetchall():
#     if id == row[0]:                         #list에서 0번째가 id
#         if pw == row[1]:                     #list에서 1번째가 pw
#             print("로그인이 되었습니다.")

# conn.commit() # 데이터베이스 값을 수정하겠다. 승인
# conn.close()

## 과제 : +4주차 쓰레드 완성하기
# 1번을 누르면 로그인
# 로그인이 되면 info테이블에서 정보를 출력(관련된 정보를 출력)
# 2번을 누르면 회원가입
# info정보를 저장되게끔(데이터베이스에)