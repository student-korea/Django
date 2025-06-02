from django.shortcuts import render,redirect
from member.models import Member

def login(request):
    if request.method =="GET":
        idCheck = request.COOKIES.get('idCheck','')
        context = {'save_id':idCheck}
        return render(request,'login.html',context)
    else: 
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        idCheck = request.POST.get('idCheck')
        
        try :
            qs =Member.objects.get(id=id,pw=pw)
        except:
            context = {'msg':0}
            return render(request,'login.html',context)
    request.session['session_id'] = id
    request.session['session_nickName'] = qs.nickName
    
    context = {'msg':1}
    reponse = render(request,'login.html',context)
    if idCheck != None:
        reponse.set_cookie('idCheck',id,max_age=60*60)
    else:
        reponse.delete_cookie('idCheck')
    return reponse

def logout(request):
    request.session.clear()
    context = {'msg':-1}
    return render(request,'index.html',context)

def join01(request):
    return render(request,'join01.html')

def join02(request):
    if request.method =="GET":
        return render(request,'join02.html')
    else: 
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        name = request.POST.get('name')
        nickName = request.POST.get('nickName')
        f_tell = request.POST.get('f_tell')
        m_tell = request.POST.get('m_tell')
        l_tell = request.POST.get('l_tell')
        tel = f"{f_tell}-{m_tell}-{l_tell}"
        gender = request.POST.get('gender')
        hobby = request.POST.getlist('hobby')
        hobby = ','.join(hobby)
        # db저장
        Member(id=id,pw=pw,name=name,nickName=nickName,tel=tel,gender=gender,hobby=hobby).save()
        
        print("넘어온 데이터 : ",id,pw,name,nickName,tel,gender,hobby)
        
        return redirect('/member/join03/')
        
def join03(request):
    return render(request,'join03.html')