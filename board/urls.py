from django.urls import path, include
from . import views

urlpatterns = [
    # path( url 패턴, 설정파일명.함수명 )
    path('', views.index),
    path('list/', views.list),
    path('view/', views.view),
    path('write/', views.write),
    path('update/', views.update),
    path('delete/', views.delete)
]