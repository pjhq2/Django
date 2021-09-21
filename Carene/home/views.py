from django.shortcuts import render
from board.models import Board

def index(request):
    board = Board.objects.order_by('-pk')[:5]
    context = {
        'board': board,
    }
    return render(request, 'home/index.html', context)