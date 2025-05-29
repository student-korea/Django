from django.shortcuts import render,redirect
from students.models import Student
# Create your views here.
def list(request):
    qs = Student.objects.all()
    context = {'list':qs}
    return render(request,'list.html',context)
def write(request):
    return render(request,'write.html')
def view(request):
    return render(request,'view.html')
def update(request):
    return render(request,'update.html')
def delete(request):
    return render(request,'update.html')
