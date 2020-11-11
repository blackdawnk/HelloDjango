from django.urls import path
from . import views


urlpatterns = [
    path('boards/', views.BoardListView.as_view()),
    path('boards/<pk>/', views.BoardDetailView.as_view()),
    path('boards/create/', views.BoardCreateView.as_view())
]

# BoardListView 클래스의 as_view가 호출될 때
# 실제로 Board 객체의 모든 내용을 직렬화해서 JSON형태로 출력

