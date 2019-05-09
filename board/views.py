from django.shortcuts import render,redirect
from .models import board
from .forms import boardForm
# Create your views here.

def list(request):
   return render(request,'board/list.html', {'list' : board.objects.all()})

def new(request):
   if request.method == "POST":
      form = boardForm(request.POST)
      if form.is_valid():
         board = form.save(commit=False)
         board.save()
         return redirect('list')
   else:
      form = boardForm()

      return render(request,'board/new.html', {'form' : form})  