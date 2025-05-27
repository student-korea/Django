from django.shortcuts import render,redirect
from students.models import Students
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def list(request):
    qs = Students.objects.all()
    context={'list':qs}
    return render(request,'students/list.html',context)
# from django.http import HttpResponse
# # Create your views here.
# def list(request):
#     # txt='''
#     #     <html>
#     #     <head></head>
#     #     <body>
#     #     <h2>학생리스트 페이지</h2>
#     #     </body>
#     #     </html>
#     # '''
#     return render(request,('students/list.html'))

def write(request):
    return render(request,'students/write.html')    

def write2(request):
    name=request.POST.get('name')
    major=request.POST.get('major')
    grade=request.POST.get('grade')
    age=request.POST.get('age')
    gender=request.POST.get('gender')
    print("데이터 정보: ",name,major,grade,age,gender)
    
    qs = Students(name=name,major=major,grade=grade,age=age,gender=gender)
    qs.save()
    return redirect('students:list')
    # return HttpResponseRedirect(reverse('students:list'))
    # return render(request,'students/write.html')    