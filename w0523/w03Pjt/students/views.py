from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def list(request):
    #return HttpResponse("리스트 페이지 연결")
    return render(request,'list.html')