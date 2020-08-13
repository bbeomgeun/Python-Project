20200708 6주차 pyqt 실습

현재 Version 5까지 나옴

PyQt - 프레임워크 vs API vs 라이브러리

라이브러리 : 어떤 사람이 특정 기능이나 기술이나 목적을 다른 사람이 갖다 사용할 수 있도록 만들어 놓은 것.
API : 라이브러리의 다음 버전 느낌. 누구나 쉽게 갖다 사용할수 있도록 좀 더 간단하게 포장해놓은 것.
 + 설명(어떤 클래스이고 어떤 명령어, 이렇게 사용할 수 있습니다.)
프레임워크 : APi와 관련 전문적인 툴과 기능을 모아 놓은 것.

1) 시간을 많이 사용하자.

2) TopDown 방식으로 공부하자.
 - 필요한 기능을 검색하자. PyQt기능~ 검색 후 어떤 위젯이나 속성을 사용하라고 알 수 있다.

 PyQt 실행 방법(PyQt + desinger = 프레임워크)
  - designer 검색 -> designer에서 PyQt의 기본 툴을 만들것이다.

  1) 위젯 - 프로그램 안에 들어가는 요소 하나하나
   - 위젯상자 : 여러 종류의 위젯들을 모아 놓은 것.

  2) 객체 탐색기 : 위젯들의 상하관계를 보여줌.

  기본 위젯들의 스타일 바꾸기 : style sheet에서 속성 변경 ( https://doc.qt.io/qt-5/stylesheet-reference.html ) 참고
  위젯들의 고유id를 설정해서 구분을 해주자.
  예시를 보자 (ctrl+r)
  저장한 파일은 ui 상태 ->파이썬이 읽을 수 있도록 바꿔주자.
  anaconda prompt-> cd후 ui가 있는 경로 설정 / 파일 변환  pyuic5 -x untitled.ui -o interface.py (pyuic5 -x 내 파일이름 -o 새로 변환할 이름)

  순서 : 디자이너로 만든다 -> py로 변환한다 -> 파이썬에서 불러와서 코드로 추가수정을 해준다.(리스너 추가)
   (하지만 코드양이 벅차므로 나눠준다) - GUIClass.py

   위젯관련 사이트 (https://wikidocs.net/37458) 참고

   레이아웃 = 적응형으로 구현할때(스페이서를 지정 안하면 화면사이즈에 맞게 늘어난다.)

   urllib.request -> 웹 크롤링

   hover ->마우스 올렸을 때 속성을 변경
   pressed, released 

    border-radius 

   D-DAY 관련 메소드 : QDateTime 객체 사용
   QDateTime은 QtCore에 소속. from PyQt5.QtCore import QDateTime 혹은 from PyQt5.QtCore import * 을 사용.
   .daysTo(QDate)	현재 DateTime과 Parameter가 몇일 차이인지 알려줍니다. Parameter로 QDate 객체를 입력합니다.
