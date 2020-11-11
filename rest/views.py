from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

from board.models import Board
from rest.serializers import BoardSerializer, BoardDetailSerializer, BoardCreateSerializer


class BoardListView(ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class BoardDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardDetailSerializer

class BoardCreateView(CreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardCreateSerializer



