from django.shortcuts import render,redirect
from board.models import Board
from django.db.models import F
# Create your views here.
def list(request):
    qs = Board.objects.order_by('-bgroup','bstep')
    content = {'list':qs}
    return render(request,'list.html',content)

def view(request,bno):
    # qs = Board.objects.get(bno=bno)
    # qs.bhit +=1
    # qs.save()
    # context = {'board':qs}
    qs = Board.objects.filter(bno=bno)
    qs.update(bhit = F('bhit')+1)
    context = {'board':qs[0]}
    return render(request,'view.html',context)

def write(request):
    if request.method =='GET':
        return render(request,'write.html')
    else :
        id = request.POST.get('id')
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        # id = request.session.session_id
        # Board(id=id,btitle=btitle,bcontent=bcontent,bfile=bfile).save()
        
        qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent,bfile=bfile)
        qs.bgroup = qs.bno
        qs.save()
        context = {'msg':1}
        return render(request,'write.html',context)
    
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
        context = {'msg':1,'board':qs}
        return render(request,'update.html',context)
    
def delete(request,bno):
    Board.objects.get(bno=bno).delete()
    return redirect('/board/list/')

def replay(request,bno):
    if request.method == 'GET':
        qs=Board.objects.get(bno=bno)
        context = {'board':qs}
        return render(request,'replay.html',context)
    elif request.method == "POST":
        id = request.POST.get("id")
        bgroup = request.POST.get("bgroup")
        bstep = int(request.POST.get("bstep"))
        bindent = int(request.POST.get("bindent"))
        btitle = request.POST.get("btitle")
        bcontent = request.POST.get("bcontent")
        bfile = request.POST.get("bfile")
        replay_qs = Board.objects.filter(bgroup=bgroup,bstep__gt=bstep)
        replay_qs.update(bstep= F('bstep')+1)
        qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent,bgroup=bgroup,bstep=bstep+1,bindent=bindent+1,bfile=bfile)
        context={'msg':1,'board':qs}
        return render(request,'replay.html',context)
    