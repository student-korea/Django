from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.db.models import F,Q
from board.models import Board
from member.models import Member
from comment.models import Comment

# Create your views here.
def list(request):
    page = int(request.GET.get('page',1))
    qs = Board.objects.all().order_by('-ntcnk','-bgroup','bstep')
    paginator = Paginator(qs,10)
    list = paginator.get_page(page)
    context = {'list':list}
    return render(request,'list.html',context)

def write(request):
    if request.method == 'GET': 
        return render(request,'write.html')
    elif request.method =='POST':
        id = request.POST.get('id')
        member = Member.objects.get(id=id)
        # id = request.session.get('session_id')
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.FILES.get('bfile','')
        ntcnk = request.POST.get('ntcnk')
        qs = Board.objects.create(member=member,btitle=btitle,bcontent=bcontent,bfile=bfile,ntcnk=ntcnk)
        qs.bgroup = qs.bno
        qs.save()
        return redirect('/board/list/')

def view(request,bno):
    print("넘어온 데이터 : ",bno)
    qs = Board.objects.filter(bno=bno)
    # 이전글
    pre_qs = Board.objects.filter(
       Q(ntcnk__lte=qs[0].ntcnk,bgroup__lt=qs[0].bgroup,bstep__lte=qs[0].bstep)|
       Q(ntcnk=qs[0].ntcnk,bgroup__lt=qs[0].bgroup)
    ).order_by('-ntcnk','-bgroup','bstep').first()
    # 다음글
    next_qs = Board.objects.filter(
       Q(ntcnk__gte=qs[0].ntcnk,bgroup__gt=qs[0].bgroup,bstep__gte=qs[0].bstep)|
       Q(ntcnk__gt=qs[0].ntcnk)
    ).order_by('ntcnk','bgroup','-bstep').first()
    
    c_qs = Comment.objects.filter(board=qs[0]).order_by('-cno')
    
    context = {'board':qs[0],'pre_board':pre_qs,'next_board':next_qs,'comment':c_qs}
    return render(request,'view.html',context)