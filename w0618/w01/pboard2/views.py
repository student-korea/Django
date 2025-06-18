from django.shortcuts import render
import requests
import json

# 공공데이터 상세보기
def view(request,galContentId):
    print('넘어온 galContentId: ',galContentId)
    # 공공데이터 호출
    dlist = publicData()
    for d in dlist:
        if int(d['galContentId']) == galContentId:
            break   
    context = {'dData':d}
    print('dData :',d)
    return render(request,'pboard2/view.html',context)


# 공공데이터 리스트
def list(request):
    dlist = publicData()
    context = {'list':dlist}
    return render(request,'pboard2/list.html',context)

# 공공데이터 가져오기 함수    
def publicData():
    public_key = '918RE13GA7OY7ZEmUzApgbOeAcQoZ%2FaHsXWcqPAKQ9YNNPj83KOstRMRIUrCFIAcm9qj2R6b7NFZjp%2FYsYzJLg%3D%3D'
    pageNo = 1
    url = f'http://apis.data.go.kr/B551011/PhotoGalleryService1/galleryList1?serviceKey={public_key}&numOfRows=10&pageNo={pageNo}&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json'
    # 웹스크래핑 requests
    response = requests.get(url)  # str타입
    
    # 문자열 -> json타입으로 변경
    json_data = json.loads(response.text)
    dlist = json_data['response']['body']['items']['item']
    
    return dlist 

def movieData():
    mpublic_key = 'b4cefdc91025f56609b0e03df7a460a0'
    url = f'https://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={mpublic_key}&targetDt=20250617'
    # 웹스크래핑 requests
    response = requests.get(url)  # str타입
    
    # 문자열 -> json타입으로 변경
    json_data = json.loads(response.text)
    mlist = json_data['boxOfficeResult']['boxofficeType']['showRange']['dailyBoxOfficeList']
    
    return mlist    