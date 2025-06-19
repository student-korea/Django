from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def oauth(request):
    code = request.GET.get('code')
    print('code : ',code)
    Content_type='application/x-www-form-urlencoded;charset=utf-8'
    grant_type='authorization_code'
    client_id='d249de78da1e2b95b77f2a3191923650'
    redirect_url = 'http://localhost:8000/kakao/oauth'
    kakao_token_url = 'https://kauth.kakao.com/oauth/token'
    request_data = {
        'grant_type':grant_type,
        'client_id':client_id,
        'redirect_url':redirect_url,
        'code':code,
    }
    
    token_headers={
       'Content-type':Content_type
    }
    
    token_data = requests.post(kakao_token_url,data=request_data,headers=token_headers)
    token_json = token_data.json()
    
    access_token =token_json.get('access_token')
    
    kakao_profile_url = 'https://kapi.kakao.com/v2/user/me'
    
    auth_headers ={
        'Authorization':f'Bearer ${access_token}',
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
    }  
    uesr_info = requests.get(kakao_profile_url,headers=auth_headers)
    user_info_json = uesr_info.json()
    print('개인정보 : ',user_info_json)
    print('token : ',token_data)
    print('회원번호 : ',user_info_json.get('id'))
    kakao_account = user_info_json.get('kakao_account')
    kakao_profile = kakao_account.get('profile')
    kakao_nickname = kakao_profile.get('nickname')
    kakao_thumbnail_image_url = kakao_profile.get('thumbnail_image_url')
    kakao_profile_image_url = kakao_profile.get('profile_image_url')
    print('카카오계정 전체정보 : ',kakao_account)
    print('카카오계정 프로필 정보 : ',kakao_profile)
    print('카카오계정 닉네임 : ',kakao_nickname)
    print('프로필 미리보기 이미지 URL : ',kakao_thumbnail_image_url)
    print('프로필 사진 URL : ',kakao_profile_image_url)
    
    # request.session.session_id = user_info_json.get('id')
    # return redirect('/')
    return HttpResponse(f'code : {code}, token json:{token_json}<br>닉네임:{kakao_nickname},<br>프로필 사진:{kakao_thumbnail_image_url}')
