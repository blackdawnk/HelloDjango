from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView

from board.models import Board
from rest.serializers import BoardSerializer, BoardDetailSerializer


class BoardListView(ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class BoardDetailView(RetrieveAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardDetailSerializer



