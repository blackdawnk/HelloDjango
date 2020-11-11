from rest_framework.serializers import ModelSerializer

from board.models import Board


class BoardSerializer(ModelSerializer):  # list
    class Meta:
        model = Board
        fields = ['id', 'title', 'userid', 'regdate',
                  'views', 'thumbup']


class BoardDetailSerializer(ModelSerializer):  # list
    class Meta:
        model = Board
        fields = ['id', 'title', 'userid', 'regdate',
                  'views', 'thumbup', 'contents']

class BoardCreateSerializer(ModelSerializer):  # list
    class Meta:
        model = Board
        fields = ['title', 'userid', 'contents']