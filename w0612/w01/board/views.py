from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.core import serializers #json타입
from django.views.decorators.csrf import csrf_exempt #csrf토큰이 없을때 예외처리
from board.models import Board

def list(request):
    qs = Board.objects.all().order_by('-ntcnk','-bgroup','bstep')
    context = {'list':qs}
    return render(request,'board/list.html',context)