from django.shortcuts import render,redirect
from member.models import Member
# Create your views here.
def login(request):
    if request.method =='GET':
        return render(request,'login.html')
    elif request.method =='POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        print("아이디 , 패스워드 : ",id,pw)
        try: 
            qs = Member.objects.get(id=id)
            if qs.pw == pw:
                request.session['session_id']=id
                txt = 1
            else:
                txt = -1
        except:
            txt = 0
        # try: 
        #     qs = Member.objects.get(id=id,pw=pw)
        #     request.session['session_id']=id
        #     #request.session.claer() 세션 삭제
        #     #del request.session['session_id'] 세션  한개삭제
        #     print(qs)
        #     txt = '1'
        # except:
        #     txt = '0'
        #     print(txt)
        context ={'msg':txt}
        return render(request,'login.html',context)
        #return redirect('/') 
def logout(request):
    request.session.clear()
    context = {'msg':2}
    return render(request,'login.html',context)
    