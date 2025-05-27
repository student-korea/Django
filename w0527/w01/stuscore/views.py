from django.shortcuts import render
from stuscore.models import Stuscore
# Create your views here.
def list(request):
    qs = Stuscore.objects.all()
    context = {'list':qs}
    return render(request,'stuscore/list.html',context)