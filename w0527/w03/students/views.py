from django.shortcuts import render

def view(request):
    name = request.GET.get("name")
    age = request.GET.get("age")
    context={"name":name,"age":age}
    return render(request,'students/view.html',context)

# Create your views here.
def list(request):
    id = request.POST.get("id")
    pw = request.POST.get("pw")
    gender = request.POST.get("gender")
    hobbys = request.POST.getlist("hobby")
    context = {"id":id,"pw":pw,"gender":gender,"hobby":hobbys}
    return render(request,'students/list.html',context)

def result(request):
    name = request.POST.get("name")
    kor = request.POST.get("kor")
    eng = request.POST.get("eng")
    total = int(kor)+int(eng)
    hobbys = request.POST.getlist("hobby")
    context = {"name":name,"kor":kor,"eng":eng,"total":total,"hobby":hobbys}
    return render(request,'students/result.html',context)

def write(request):
    return render(request,"students/write.html")

def send(request,name,age):
    print("전달받은 값 : ",name,age)
    context={"name":name,"age":age}
    return render(request,'students/send.html',context)
    