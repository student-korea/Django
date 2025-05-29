from django.shortcuts import render,redirect
from students.models import Student

# Create your views here.
def list(request):
    qs = Student.objects.all()
    context={'list':qs}
    return render(request,'list.html',context)

def write(request):
    if request.method =='GET':
        return render(request,'write.html') 
    else :
        name = request.POST.get('name')
        major = request.POST['major']
        grade = request.POST['grade']
        age = request.POST['age']
        gender = request.POST['gender']
        hobby = request.POST.getlist('hobby')
        hobby = ','.join(hobby)
        Student(name=name,major=major,grade=grade,age=age,gender=gender,hobby=hobby,memo='등록합니다.').save()
        return redirect('/students/list/')
    
def view(request,no):
    try:
        qs = Student.objects.get(no=no)
    except:
        qs =None
    context = {'stu':qs}
    return render(request,'view.html',context)

def update(request,no):
    if request.method =='POST':
        no = request.POST.get('no')
        qs = Student.objects.get(no=no)
        qs.name=request.POST.get('name')
        qs.major=request.POST.get('major')
        qs.grade=request.POST.get('grade')
        qs.age=request.POST.get('age')
        qs.gender=request.POST.get('gender')
        hobby = request.POST.getlist('hobby')
        hobby = ','.join(hobby)
        qs.hobby=hobby
        qs.save()
        return redirect(f'/students/view/{no}/')
    else :
        qs = Student.objects.get(no=no) # 해당되는 학생정보검색
        context = {'stu':qs}
        return render(request,'update.html',context)
    
def delete(request,no):
    qs = Student.objects.get(no=no) 
    qs.delete()
    return redirect('/students/list/')