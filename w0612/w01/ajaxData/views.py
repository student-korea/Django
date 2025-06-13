from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from board.models import Board

def blist(request):
    qs = Board.objects.all().order_by('-ntcnk','-bgroup','bstep')
    l_qs = list(qs.values())
    context = {'result':'success','list':l_qs}
    return JsonResponse(context)

def bwrite(request):
    id = request.POST.get('id')
    btitle = request.POST.get('btitle') 
    bcontent = request.POST.get('bcontent')
    qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent)
    qs.bgroup=qs.bno
    qs.save()
    l_qs = list(Board.objects.filter(bno=qs.bno).values())
    context = {'result':'success','board':l_qs}
    return JsonResponse(context)

def bdelete(request):
    bno = request.POST.get('bno')
    Board.objects.get(bno=bno).delete()
    context = {'result':'success'}
    return JsonResponse(context)