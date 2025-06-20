from django.shortcuts import render
from django.http import JsonResponse
from comment.models import Comment
# 하단댓글리스트
def clist(request):
    cno = request.POST.get('cno')
    Comment.objects.get(cno=cno).delete()
    context = {'msg':'success'}
    return render(request,'list.html',context)

def cdelete(request):
    context = {}
    return JsonResponse(context)