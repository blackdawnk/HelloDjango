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
```
urlpatterns = [
    path('board/', views.index)
]
```
* url : localhost:8000/board
* 순서
```
board/views.py
def index:
    return HttpResponse('')
```
------
# URL 맵핑 (분리 연결)
* config/urls.py 수정
```
urlpatterns = [
    path('board/', include('board.urls'))
]
```
* url : localhost:8000/board
* 순서
```
board/urls.py
board/views.py
def index:
    return HttpResponse('')
```
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
```
config/settings.py
TEMPLATES {'DIRS': [BASE_DIR / 'templates'] }
```
------
# 정적 자원 (assets) 할당
* css, img, js 등의 파일을 static web assets 라고 함
* 정적 자원을 관리하기 위해 config/settings.py에 static 이라는 항목을 사용
    - static 디렉토리 밑에 bs4, css, fa47, img 등의 폴더를 넣음
```
config/settings.py
STATICFILES_DIRS = [ BASE_DIR / 'static' ]
```
```
{% load static}  # 시작 위치 지정
<input type="text" value="{% static '파일경로' %}">
```
    
------
# 템플릿 확장
* 공통적으로 사용되는 html코드를 기본 템플릿으로 만들고 각 페이지마다 변경이 필요한 부분만 코드로 작성하게 하는 템플릿 확장 기능
* 사용법
    - base.html
        - 공통적인 부분을 작성하고 메인이 들어갈 부분에 {% block content %} {% endblock %}을 작성
    - main.html
        - 기본문서 불러오기 : {% extends 'base.html' %}
        - {% block content %}와 {% endblock %} 사이에 메인 소스 작성
```
base.html
<html>
    <head> </head>
    <body>
        {% block content %}
        {% endblock %}
    </body>
</html>
```
```
main.html
{% extends 'base.html' %}
        {% block content %}
            메인 소스
        {% endblock %}
```
------
# 모델
* Django는 ORM(Object Relation Mapping)기능을 사용하기 때문에 SQL쿼리 없이 DB관련 작업 가능
* Model의 클래스를 생성하면, 해당 모델에 상응하는 테이블을 자동으로 만들어 줌
* django에서 제공하는 Model API를 이용해서 데이터 작업을 수행할 수 있음
* 현재 사용 중인 데이터베이스 정보는 config/settings.py의 DATABASES를 확인
    - 기본 DB : django.db.backends.sqlite3 (내장형 디비)
    - 다른 DB로 변경 가능 (host, user, pw, port 등이 필요)
    - mysql  :　django.db.backends.mysql
    - oracle :　django.db.backends.oracle
------
# 게시판 모델 생성
* config/settings.py의 INSTALLED_APPS에 추가
    - 'board.apps.BoardConfig'
    - 직접 생성하지 않은 BoardConfig는 apps.py에 자동 생성될 예정
    - python manage.py makemigrations   (터미널에 입력)
        - 모델 생성시 사용된 SQl문을 확인하려면 sqlmigrate 명령 사용
    - python manage.py migrate  (터미널에 입력)
        - board/models.py에 작성한 class를 테이블로 생성
* 테이블 구조 변경
    1. models.py의 클래스 내용을 변경
    2. python manage.py makemigrations
    3. python manage.py migrate
* 테이블 삭제
    1. board/migrations의 0001_~~.py 파일 제거
    2. db.sqlite3의 migrations 테이블에 0001_~~.py 데이터 제거
    3. python manage.py makemigrations
    4. python manage.py migrate
------
# Django 모델 APi
* Django 모델에 CRUD 사용을 위해 Django shell 사용
```python manage.py shell```
* 모델을 패키지처럼 불러오기
```form board.models import Board```
* 삽입 (insert)
```{.python}
b = Board(title='이글이 보이나요?', userid='ming', contents='하히후헤호')
b.save()
```

* 조회 (select)
    - all : 모델에 저장된 모든 데이터 조회, 기본적으로 id만 출력
        - Board.objects.all()
    - get : 조건을 만족하는 데이터 1건만 조회, Board 모델 리턴
    - filter : 조건을 만족하는 데이터들을 조회, QuerySet 리턴
- 조회 : all
```{.python}
s = ''
for row in Board.objects.all():
    s+= str(row.id) + '/' + row.title + '\n'
print(s)
```
- 단일 데이터 조건 조회 : get
```
Board.objects.get(id=1)
Board.objects.get(title__contains='이글')
```
- 다중데이터 조건 조회 : filter
```
Board.objects.filter(id=1)
Board.objects.filter(title__contains='이글')
```
- 수정 (update)
```
b = Board.objects.get(id=1)
b.title = '수정됨‘
b.save()
```
- 삭제 (delete)
```
b = Board.objects.get(id=1)
b.delete()
```
- 기타
    - 조회된 모델 개수 : count
    - 모델 조회시 정렬 : order_by
    - 모델 조회시 중복 제외 : distinct
```
Board.objects.count('id')
```
```
Board.objects.order_by('id')
Board.objects.order_by('-id')	# 내림차순
```
```
Board.objects.distinct('name')
```
* 그외 질의문
    - [django document 바로가기](docs.djangoproject.com/en/3.1/topics)
------
# django Admin
* django admin은 장고에서 기본적으로 제공하는 관리자 앱
* django에 생성된 모델을 조회하고 추가, 수정, 삭제 할 수 있음
* 접속 가능한 계정 생성
    - python manage.py createsuperuser
* python admin 접속
    - python manage.py runserver
    - localhost:8000/admin
* django admin에서 모델 관리
    - board/admin.py에 다음 내용 추가
```
admin.site.register('모델명')
admin.site.register(Board)
```
* django admin에서 특정 모델 검색
    - board/admin.py에 다음 내용 추가
```
class BoardAdmin(admin.ModelAdmin):
    search_fields = ['title']
	list_display = ['id', 'title', 'userid', 'regdate']
	list_filter = ['title', 'userid', 'regdate']
admin.site.register(Board, BoardAdmin)
```
------
# 뷰
* django에서 뷰는 다른 MVC 프레임워크에서 말하는 컨트롤러와 비슷한 역할
* view는 작업에 필요한 데이터를 모델 또는 외부에서 가져와서 적절히 가공해서 템플릿으로 넘기는 일을 수행
* 게시판 목록 출력
    1. board/urls.py에 urlpatterns 수정
    2. board/views.py에 list, view 함수 수정
    3. list.html, view.html 파일 수정

- board/urls.py
```
urlpatterns = [
    ...
    path('view/<int:bid>/', views.view),    # <자료형:변수명>
    ...
]
```
* 버튼 링크 지정
    1. board/urls.py에 urlpatterns 수정
    2. html 태그 수정
- board/urls.py
```
urlpatterns = [
    ...
    path('list/', views.list, name='list'),     # {% url board:list %} 에서 list name 지정
    ...
]
```
- html 태그 수정
```
<a href="{% url 'board:list' %}"></a>
```
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
    
