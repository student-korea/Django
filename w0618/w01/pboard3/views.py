from django.shortcuts import render
from django.http import JsonResponse
import requests
import json

# 공공데이터 상세보기
def view(request,galContentId):
    print('넘어온 galContentId: ',galContentId)
    # 공공데이터 호출
    dlist = movieData()
    for d in dlist:
        if int(d['galContentId']) == galContentId:
            break   
    context = {'dData':d}
    print('dData :',d)
    return render(request,'pboard3/view.html',context)


# 공공데이터 리스트
def list(request):
    day = request.POST.get('day')
    if day is not None:
        try:
            day = int(day)
        except:
            day = 20250617
    else:
        day = 20250617
    mlist = movieData(day)
    context = {'list':mlist}
    return render(request,'pboard3/list.html',context)
# 공공데이터 리스트
def jlist(request):
    day = request.POST.get('day')
    print('|',day)
    if day is not None:
        try:
            day = int(day)
        except:
            day = 20250617
    else:
        day = 20250617
    mlist = movieData(day)
    print(" | ",mlist)
    return JsonResponse(list(mlist))


def movieData(day):
    public_key = 'b4cefdc91025f56609b0e03df7a460a0'
    url = f'https://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={public_key}&targetDt={day}'
    # 웹스크래핑 requests
    response = requests.get(url)  # str타입
    print(url)
    # 문자열 -> json타입으로 변경
    json_data = json.loads(response.text)
    mlist = json_data['boxOfficeResult']['dailyBoxOfficeList']
    
    return mlist    