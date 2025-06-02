from django.shortcuts import render,redirect
from board.models import Board
# Create your views here.

def list(request):
    return render(request,'list.html')

def write(request):
    if request.method=='GET':
        return render(request,'write.html')
    elif request.method=='POST':
        id='aaa'
        btitle=request.POST.get('btitle')
        bcontent=request.POST.get('bcontent')
        bfile=request.POST.get('bfile')
        
        qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent)
        qs.bgroup = qs.bno
        qs.save()
        return redirect('board:list')