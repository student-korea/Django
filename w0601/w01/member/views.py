from django.shortcuts import render,redirect
from member.models import Member  #Member테이블 호출

# 로그아웃 부분
def logout(request):
    # session 모두 삭제
    request.session.clear()
    context = {'msg':-1}
    return render(request,'login.html',context)


# 로그인 부분
def login(request):
    # 쿠키 읽어오기
    cookie_info = request.COOKIES
    # 있으면 :aaa, 없으면 None -> '' 빈공백처리
    cook_id = request.COOKIES.get('cookie_val','')  
    print("cook_id : ",cook_id)
    context = {'cookie_info':cookie_info, 'cook_id':cook_id}
    
    if request.method == 'GET':  # 로그인페이지 열기
        return render(request,'login.html',context)
    # 아이디저장 체크박스
    elif request.method == 'POST': # ID,PW확인
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        cookie_val = request.POST.get('cookie_val')
        
        # 쿠키저장
        
        # id,pw확인 - 없을때 error발생 예외처리
        try:
            qs = Member.objects.get(id=id,pw=pw)
            ## session 추가
            request.session['session_id'] = qs.id
            request.session['session_nickName'] = qs.nickName
            msg = 1  # id,pw가 있음.
            print("데이터 여부 : 존재함")
        except:
            msg = 0  # id,pw가 없음.
            print("데이터 여부 : 없음")
        
        context = {"msg":msg, 'cookie_info':cookie_info,'cook_id':cook_id}
        
        response = render(request,'login.html',context)
        # response 쿠키저장
        if cookie_val is not None:
            #cookie_val = 'idsave' 60초*60분*24시간*365일
            response.set_cookie('cookie_val',id,max_age=60*60*24*365)  
        else:
            response.delete_cookie('cookie_val')
        
        return response
    
def join01(request):
    return render(request,'join01.html')

def join02(request):
    if request.method =='GET':
        return render(request,'join02.html')
    elif request.method =='POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        pw2 = request.POST.get('pw2')
        name = request.POST.get('name')
        nickName = request.POST.get('nickname')
        f_tell = request.POST.get('f_tell')
        m_tell = request.POST.get('m_tell')
        l_tell = request.POST.get('l_tell')
        tel = f"{f_tell}-{m_tell}-{l_tell}"
        gender = request.POST.get('gender')
        hobby = request.POST.getlist('hobby')
        hobby = ','.join(hobby)
        Member(id=id,pw=pw,name=name,nickName=nickName,tel=tel,gender=gender,hobby=hobby).save()
        print("넘어온 데이터 : ",id,pw,pw2,name,nickName,tel,gender,hobby)
        return redirect('/member/join03/')
    

def join03(request):
    return render(request,'join03.html')
    
        
        