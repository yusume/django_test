from django.shortcuts import render
from .models import board
# Create your views here.

def list(request):
   return render(request,'board/list.html', {'list' : board.objects.all()})