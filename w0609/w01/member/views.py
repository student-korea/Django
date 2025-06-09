from django.shortcuts import render,redirect
from member.models import Member

# Create your views here.
def login(request):
    if request.method =='GET':
        cook_id = request.COOKIES.get('cook_id','')
        context = {'cook_id':cook_id}
        return render(request,'login.html',context)
    else:
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        idsave = request.POST.get('idsave')
        msg=0
        try:
            qs = Member.objects.get(id=id,pw=pw)
            request.session['session_id']=id
            msg=1
        except: pass
        cook_id = request.COOKIES.get('cook_id','')
        context = {'msg':msg,'cook_id':cook_id}
        response = render(request,'login.html',context)
        if idsave:
            response.set_cookie('cook_id',id,max_age=60*60*24*30)
        else:
            response.delete_cookie('cook_id')
        return response
    
def logout(request):
    request.session.clear()
    context = {'msg':-1}
    return render(request,'login.html',context)

def step01(request):
    return render(request,'step01.html')

def step02(request):
    return render(request,'step02.html')

def step03(request):
    if request.method == 'GET':
        return render(request,'step03.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        id = request.POST.get('id')
        email1 = request.POST.get('email1')
        email2 = request.POST.get('email2')
        email = f'{email1}@{email2}'
        emailc = request.POST.get('emailc')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        phone1 = request.POST.get('phone1')
        phone2 = request.POST.get('phone2')
        phone3 = request.POST.get('phone3')
        phone = f'{phone1}-{phone2}-{phone3}'
        tel1 = request.POST.get('tel1')
        tel2 = request.POST.get('tel2')
        tel3 = request.POST.get('tel3')
        tel = f'{tel1}-{tel2}-{tel3}'
        birth1 = request.POST.get('birth1')
        birth2 = request.POST.get('birth2')
        birth3 = request.POST.get('birth3')
        birth = f'{birth1}-{birth2}-{birth3}'
        corporate = request.POST.get('corporate')
        gender = request.POST.get('gender')
        hobbys = request.POST.getlist('hobby')
        hobby = ','.join(hobbys)
        print("넘어온 데이터 : ",name,id,email,emailc,address1,address2
              ,phone,tel,birth,corporate,gender,hobby)
        
        Member.objects.create(name=name,id=id,email=email,emailc=emailc,address1=address1,address2=address2
              ,phone=phone,tel=tel,birth=birth,corporate=corporate,gender=gender,hobby=hobby)
        return redirect('/member/step04/{name}/')
    
def step04(request,name):
    return render(request,'step04.html')