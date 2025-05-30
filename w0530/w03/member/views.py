from django.shortcuts import render,redirect
from member.models import Member

def login(request):
    if request.method =='GET':
        return render(request,'login.html')
    elif request.method =='POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        cookie_val = request.POST.get('cookie.val')
        cook_id = request.COOKIES.get('cookie_val')
        try: 
            qs = Member.objects.get(id=id)
            if qs.pw == pw:
                request.session['session_id']=id
                txt = 1
            else:
                txt = -1
        except:
            txt = 0
        cookie_info = request.COOKIES
        context ={'msg':txt,'cookie_info': cookie_info,'cookie_id': cook_id}
        response =  render(request,'login.html',context)
        if cookie_val is not None:
            response.set_cookie('cookie_val',cookie_val,max_age = 60*60*24*365)
        else:
            response.delete_cookie('cookie_val')
            
        return response
def logout(request):
    request.session.clear()
    context = {'msg':2}
    return render(request,'login.html',context)
    