from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from students.models import Student

# Create your views here.
def list(request):
    qs =Student.objects.all()
    context ={'list':qs,'count':100,'id':'aaa'}
    return render(request,'list.html',context)

def write(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        major=request.POST.get('major')
        grade=request.POST.get('grade')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        print("입력된 정보 : ",name,major,grade,age,gender)
        Student(name=name,major=major,grade=grade,age=age,gender=gender).save()
        print("Student 객체 저장")
        return redirect('/students/list/')
    else:
        print("request.method",request.method)
        return render(request,'write.html')

def view(request):
    name = request.GET.get('name')
    qs = Student.objects.get(name=name)
    context = {'stu':qs}
    return render(request,'view.html',context)

def update(request,name):
    if request.method=='GET':
        qs = Student.objects.get(name=name)
        context = {'stu':qs}
        return render(request,'update.html',context)
    else:
        name2=request.POST.get('name')
        major=request.POST.get('major')
        grade=request.POST.get('grade')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        print("입력된 정보 : ",name2,major,grade,age,gender)
        qs =Student.objects.get(name=name)
        qs.name=name2
        qs.major=major
        qs.grade=grade
        qs.age=age
        qs.gender=gender
        qs.save()
        print("Student 객체 저장")
        return redirect('/students/list/')
    
def delete(request,name):
    print("삭제 이름: ",name)
    qs =Student.objects.get(name=name)
    qs.delete()
    return redirect('/students/list/')