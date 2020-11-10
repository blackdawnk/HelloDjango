from django.urls import path, include
from . import views


app_name = 'board'      # {% url board:list %} 에서 board namespace 지정

urlpatterns = [
    # path( url 패턴, 설정파일명.함수명 )
    path('', views.index),
    path('list/', views.list, name='list'),     # {% url board:list %} 에서 list name 지정
    path('view/<int:bid>/', views.view),
    path('write/', views.write, name='write'),
    path('update/<int:bid>/', views.update),
    path('delete/<int:bid>/', views.delete)
]