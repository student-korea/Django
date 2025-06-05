from django.shortcuts import render,redirect
from board.models import Board
from django.db.models import F,Q
from django.core.paginator import Paginator

def list(request):
    # 현재페이지 int변경
    page = int(request.GET.get('page',1)) # 없을때, 1페이지로 넘겨줌
    #search으로 넘어올때
    search = request.GET.get('search','') 
    category = request.GET.get('category','')
    print('검색데이터 : ',category,search)
    
    if search == '':  # 일반리스트로 넘어온 경우
        # 게시글 전체 가져오기
        qs = Board.objects.order_by('-bgroup','bstep')
        # 페이지 분기
        paginator = Paginator(qs,20) # 100개 -> 10개씩 쪼개서 전달해줌.
        list = paginator.get_page(page)  # 현재페이지에 해당되는 게시글 전달
        context = {"list":list,'page':page}
        return render(request,'list.html',context)
    else:            # 검색으로 넘어온 경우
        # 게시글 전체 가져오기  and:& or:| not:~
        if category == 'all':
            qs = Board.objects.filter(
                Q(btitle__contains=search) | Q(bcontent__contains=search))
        elif category == 'btitle':
            qs = Board.objects.filter(btitle__contains=search)
        else:
            qs = Board.objects.filter(bcontent__contains=search)
        
        # 페이지 분기
        paginator = Paginator(qs,10) # 100개 -> 10개씩 쪼개서 전달해줌.
        list = paginator.get_page(page)  # 현재페이지에 해당되는 게시글 전달
        context = {"list":list,'page':page,'category':category,'search':search}
        return render(request,'list.html',context)
    
def view(request,bno):
    # qs = Board.objects.get(bno=bno)
    # qs.bhit +=1
    # qs.save()
    # context = {'board':qs}
    category = request.GET.get('category','')
    search = request.GET.get('search','')
    
    qs = Board.objects.filter(bno=bno) # 리스트
    qs.update(bhit = F('bhit')+1) #save까지 됨.
    context = {'board':qs[0],'category':category,'search':search}
    
    return render(request,'view.html',context)

def write(request):
    if request.method =='GET':
        return render(request,'write.html')
    else :
        id = request.POST.get('id')
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        # bfile = request.POST.get('bfile')

        bfile = request.FILES.get('bfile','')
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
        bfile_pre = request.POST.get('bfile_pre','')
        bfile = request.FILES.get('bfile','')
        if not bfile:
            bfile=bfile_pre
        qs = Board.objects.get(bno=bno)
        qs.btitle=btitle
        qs.bcontent=bcontent
        qs.bfile=bfile
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
        bfile = request.FILES.get("bfile",'')
        replay_qs = Board.objects.filter(bgroup=bgroup,bstep__gt=bstep)
        replay_qs.update(bstep= F('bstep')+1)
        qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent,bgroup=bgroup,bstep=bstep+1,bindent=bindent+1,bfile=bfile)
        context={'msg':1,'board':qs}
        return render(request,'replay.html',context)
    