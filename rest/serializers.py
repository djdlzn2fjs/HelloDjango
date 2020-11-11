from rest_framework.serializers import ModelSerializer
from board.models import Board



class BoardSerializer(ModelSerializer): # list
    class Meta:
        model = Board
        files = ['id', 'title', 'userid', 'regdate', 'views', 'thumbup']


class BoardDetailSerializer(ModelSerializer): # view
    class Meta:
        model = Board
        files = ['id', 'title', 'userid', 'regdate', 'views', 'thumbup', 'contents']

