from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.core import serializers #json타입
from django.views.decorators.csrf import csrf_exempt #csrf토큰이 없을때 예외처리
from board.models import Board

    
def ajax3(request):
    qs = Board.objects.all().order_by('-ntcnk','-bgroup','bstep')
    a= request.POST.get('sampleId')
    list_qs = serializers.serialize('json',[qs])
    context = {'result':'성공','list':list_qs}
    return JsonResponse(context)

def bwrite(request):
    id = request.POST.get('id')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent)
    qs.bgroup = qs.bno
    qs.save()
    
    l_qs = list(Board.objects.filter(bno=qs.bno).values())
    context = {'result':'success','board':l_qs}
    return JsonResponse(context)