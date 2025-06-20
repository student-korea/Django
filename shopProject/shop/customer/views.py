from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from customer.models import Customer
from comment.models import Comment
from member.models import Member
import datetime
from django.db.models import F
# Create your views here.
def list(request):
    page = int(request.GET.get('page',1))
    qs = Customer.objects.all().order_by('-ntchk','-bgroup','bstep')
    paginator = Paginator(qs,10)
    customerList = paginator.get_page(page)
    context = {'list':customerList,'page':page}
    return render(request,'list.html',context)

def view(request,bno):
  # db연결
  qs = Customer.objects.filter(bno=bno)
  # comment db연결
  c_qs = Comment.objects.filter(customer=qs[0])
  context = {'customer':qs[0],'clist':c_qs}
  response = render(request,'view.html',context)
  
  
  # 쿠키이름 지정 - cookie_bhit:aaa, cookie_bhit:bbb, cookie_bhit:아이디
  cookie_name = f'cookie_bhit:{request.session["session_id"]}'
  
  # 쿠키시간설정 - 1일기준
  #   tomorrow = datetime.datetime.now()  # 현재시간
  # 해당일의 마지막 시간으로 설정
  tomorrow = datetime.datetime.replace(datetime.datetime.now(),
                                       hour=23,minute=59,second=59)
  # 쿠키시간으로 설정형태 변경
  expires = datetime.datetime.strftime(tomorrow,"%a, %d-%b-%Y %H:%M:%S GMT")
  
  if request.COOKIES.get(cookie_name) is not None:
      cookies = request.COOKIES.get(cookie_name) #쿠키가져오기
      print('쿠키 : ',cookies)
      cookies_list = cookies.split('|')  # 101|20|100|97 -> [101,20,100,97]
      # 비교타입 - str타입   cookie_bhit:aaa    103|101
      if str(bno) not in cookies_list:
          response.set_cookie(cookie_name,cookies+f'|{bno}',expires=expires)
          qs.update(bhit=F('bhit')+1) # 조회수1증가
      
  else:
      #  쿠키이름 : cookie_bhit:aaa
      response.set_cookie(cookie_name,bno,expires=expires)
      qs.update(bhit = F('bhit')+1)   # qs.bhit += 1
  
  return response

def write(request):
    if request.method == 'GET':
        return render(request,'write.html')
    else:
        btitle = request.POST.get('btitle')
        id= request.session['session_id']
        member = Member.objects.get(id=id)
        bcontent = request.POST.get('bcontent')
        bfile = request.FILES.get('bfile')
        bfile2 = request.FILES.get('bfile2')
        qs = Customer.objects.create(btitle=btitle,member=member,bcontent=bcontent,bfile=bfile,bfile2=bfile2)
        qs.bgroup = qs.bno
        qs.save()
        context = {'msg':1}
        return render(request,'write.html',context)
    
def delete(request,bno):
    if request.session['session_id']:
        Customer.objects.get(bno=bno).delete()
        context = {'msg':-1}
    else:
        context = {'msg':-2}    
    return render(request,'view.html',context)
    # return redirect('/customer/list/')

def update(request,bno):
    if request.method == 'GET':
        qs = Customer.objects.get(bno=bno)
        context = {'customer':qs}
        return render(request,'update.html',context)
    
    elif request.method == 'POST':
        # db가져오기
        qs = Customer.objects.get(bno=bno)
        # 넘어온 데이터
        qs.btitle = request.POST.get('btitle')
        qs.bcontent = request.POST.get('bcontent')
        
        # 이미지 파일첨부가 있으면
        if request.FILES.get('bfile'):
            qs.bfile = request.FILES.get('bfile')
            
        # 이미지 파일첨부2가 있으면
        if request.FILES.get('bfile2'):
            qs.bfile2 = request.FILES.get('bfile2')
        
        qs.save()     
        context = {'msg':1,'bno':bno}
        return render(request,'update.html',context)
        