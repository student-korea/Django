# Create your views here.
from django.shortcuts import render
from home.models import Member,Tag

def view(request, id):
    qs = Member.objects.get(id=id)
    tags_info = []

    for tag in qs.tags.all():
        # Tag 객체의 count를 1 증가
        tag.count +=1
        # 변경된 count 값을 데이터베이스에 저장
        tag.save() 
        tags_info.append({
            'name': tag.name,
            'count': tag.count, # 증가된 count 값을 포함
        })

    context = {
        'list': qs,
        'tags_info': tags_info,
    }
    
    return render(request, 'view.html', context)
