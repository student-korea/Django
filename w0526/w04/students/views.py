from django.shortcuts import render
from students.models import Students
# Create your views here.
def list(request):
    qs = Students.objects.all()
    context={'list':qs}
    return render(request,'list.html',context)
