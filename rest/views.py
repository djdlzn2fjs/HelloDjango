from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView

from board.models import Board
from rest.serializers import BoardSerializer, BoardDetailSerializer


class BoardListView(ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class BoardListView(RetrieveAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardDetailSerializer