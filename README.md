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
* 최종 URL : config/urls.py + board/urls.py
* 'board/' + '' = 'board/'
------
# 템플릿
* MVC 패턴이 아닌 MTV패턴을 이용
* Model : 데이터 표현
* Template : HTML 생성 목적 컴포넌트
* View : HTTP 요청(Request)에 따른 처리 결과를 HTTP 응답(Response)을 리턴하는 컴포넌트로 controller 역할

* board/urls.py에 url에 대응하는 view함수를 선언
* board/views.py 파일에 url에 대응하는 view 함수를 정의
* render() 함수에 정의한 템플릿 파일(html)을 작성
    - config/settings.py에 정의한 위치에 작성
    - TEMPLATES {'DIRS': [BASE_DIR / 'templates'] }
------
# 정적 자원 (assets) 할당
* css, img, js 등의 파일을 static web assets 라고 함
* 정적 자원을 관리하기 위해 config/settings.py에 static 이라는 항목을 사용
    - config/settings.py
    - STATICFILES_DIRS = [ BASE_DIR / 'static' ]
    - static 디렉토리 밑에 bs4, css, fa47, img 등의 폴더를 넣음
    - 사용
        - 시작 : {% load static}
        - 태그 옵션 value : "{% static '파일경로' %}"
------
# 템플릿 확장
* 공통적으로 사용되는 html코드를 기본 템플릿으로 만들고 각 페이지마다 변경이 필요한 부분만 코드로 작성하게 하는 템플릿 확장 기능
* 사용법
    - base.html
        - 공통적인 부분을 작성하고 메인이 들어갈 부분에 {% block content %} {% endblock %}을 작성
    - main.html
        - 기본문서 불러오기 : {% extends 'base.html' %}
        - {% block content %}와 {% endblock %} 사이에 메인 소스 작성
------
# git 계정 연동 아이디 확인 및 변경
* github에 소스를 commit/ push 할 때 사용하는 계정
    1. 확인
        - git config user.name
        - git config user.email
    2. 변경
        - git config --global user.name 변경할이름
        - git config --global user.email 변경할이메일
-----
# Push 할 때 오류 발생하면, 윈도우 자격증명을 수정
    - 제어판 - 사용자계정 - 자격증명관리 - windows 자격증명 - github 항목 삭제 후 다시 github 계정 수정
    
