from django.forms import ModelForm

from board.models import Board


class BoardForm(ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'userid', 'contents']

        # labels = [
        #     'userid': '사용자명',
        #     'title': '제목',
        #     'contents': '내용'
        # ]
