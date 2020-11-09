# HelloDjango 기본 설치 및 구동
* 장고 패키지 설치
    - pip install django
* 장고 프로젝트 생성
    - django-admin startproject config .
* 웹 사이트 구동
    - python manage.py runserver
* 장고 Board App 생성
    - django-admin startapp board
------
# URL 맵핑 (직접 연결)
* config/urls.py 수정
    urlpatterns = [
        path('board/', views.index)
    ]
* url : localhost:8000/board
* 순서 : board/views.py => def index: return HttpResponse('')
------
# URL 맵핑 (분리 연결)
* config/urls.py 수정
    urlpatterns = [
        path('board/', include('board.urls'))
    ]
* url : localhost:8000/board
* 순서 : board/urls.py -> board/views.py => def index: return HttpResponse('')
------
# 최종 URL 분석 방법
- 최종 URL : config/urls.py + board/urls.py
- 'board/' + '' = 'board/'
------
# git 계정 연동 아이디 확인 및 변경
* github에 소스를 commit/ push 할 때 사용하는 계정
    1. 확인
        - git config user.name
        - git config user.email
    2. 변경
        - git config --global user.name 변경할이름
        - git config --global user.name 변경할이름
-----
# Push 할 때 오류 발생하면, 윈도우 자격증명을 수정
    - 제어판 - 사용자계정 - 자격증명관리 - windows 자격증명 - github 항목 삭제 후 다시 github 계정 수정
    
