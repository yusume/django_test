from django.shortcuts import render,redirect,get_object_or_404
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

def edit(request, pk):
   edit_board = get_object_or_404(board, pk=pk)
   if request.method == "POST":
      form = boardForm(request.POST, instance=edit_board)
      if form.is_valid():
         edit_board = form.save(commit=False)
         edit_board.save()
         return redirect('list')
   else:
      form = boardForm(instance=edit_board)

   return render(request,'board/edit.html', {'form': form,'pk':edit_board.pk})     

def remove(request, pk):
   edit_board = get_object_or_404(board, pk=pk)
   edit_board.delete()
   return redirect('list')