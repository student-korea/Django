from django.shortcuts import render
# ajax전송에 필요한 선언
from django.http import JsonResponse
from board.models import Board
from django.core import serializers


def list3(request):
    qs = Board.objects.all().order_by('-ntcnk','-bgroup','bstep')
    context = {'list':qs}
   
    return render(request,'board/list3.html',context)
    
def ajax3(request):
    qs = Board.objects.all().order_by('-ntcnk','-bgroup','bstep')
    a= request.POST.get('sampleId')
    list_qs = serializers.serialize('json',[qs])
    context = {'result':'성공','list':list_qs}
    return JsonResponse(context)

def ajaxWrite(request):
    id = request.POST.get('id')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent)
    qs.bgroup = qs.bno
    qs.save()
    
    l_qs = list(Board.objects.filter(bno=qs.bno).values())
    context = {'result':'success','board':l_qs}
    return JsonResponse(context)

def list2(request):
    if request.method =='GET':
        qs = Board.objects.all().order_by('-ntcnk','-bgroup','-bstep')
        context = {'list':qs}
        return render(request,'board/list2.html')
    elif request.method =='POST':
        return render(request,'board/list2.html')

def view2(request,bno):
    qs = Board.objects.get(bno-bno)
    context = {'board',qs}
    
    return render(request,'board/view2.html',context)


def view(request):
    # html에서 데이터 전달
    bno = request.POST.get('bno')
    qs = Board.objects.get(bno-bno)
    # 데이터를 html전송
    context = {'board':qs,}
    return render(request,'board/view.html',context)

def list(request):
    if request.method =='GET':
        return render(request,'board/list.html')
    elif request.method =='POST':
        return render(request,'board/list.html')