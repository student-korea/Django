from django.shortcuts import render,redirect
from board.models import Board
# Create your views here.

def list(request):
    qs = Board.objects.all().order_by('-bno')
    context={'list':qs}
    return render(request,'list.html',context)
    
def write(request):
    if request.method=='GET':
        return render(request,'write.html')
    elif request.method =='POST':
        id = 'aaa'
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        qs = Board.objects.create(id = id,btitle=btitle,bcontent=bcontent)
        qs.bgroup= qs.bno
        qs.save()
        print('데이터 확인: ',btitle,bcontent,bfile)
        print('데이터 추가: ',qs.bgroup,qs.bstep,bfile)
        return redirect('board:list')
    
def view(request,bno):
    qs = Board.objects.get(bno=bno)
    context = {'board':qs}
    return render(request,'view.html',context)

def update(request,bno):
    if request.method == 'GET':
        qs = Board.objects.get(bno=bno)
        context = {"board":qs}
        return render(request,'update.html',context)
    elif request.method == "POST":
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        qs = Board.objects.get(bno=bno)
        qs.btitle=btitle
        qs.bcontent=bcontent
        qs.save()
        context = {'msg':1}
        return render(request,'update.html',context)