from django.shortcuts import render
from home.models import Member,Tag
from collections import defaultdict
import json
import random

def index(request):
    members = list(Member.objects.all())

    tag_counter = defaultdict(int)
    for member in members:
        for tag in member.tags.all():
            tag_counter[tag.name] += tag.count
            
    if all(count == 0 for count in tag_counter.values()):
        random.shuffle(members)

    else:
        sorted_tags = sorted(tag_counter.items(), key=lambda x: x[1], reverse=True)
        tag_order = [name for name, _ in sorted_tags]

        sorted_members = []
        added_ids = set()

        for tag_name in tag_order:
            group = []
            for member in members:
                if member.id in added_ids:
                    continue
                if any(tag.name == tag_name for tag in member.tags.all()):
                    group.append(member)

            random.shuffle(group)  
            sorted_members.extend(group)
            added_ids.update([m.id for m in group])

        remaining = [m for m in members if m.id not in added_ids]
        random.shuffle(remaining)
        sorted_members.extend(remaining)

        members = sorted_members

    # 6. JSON 변환
    result_list = []
    for member in members:
        tags_list = [{'name': tag.name, 'count': tag.count} for tag in member.tags.all()]
        result_list.append({
            'id': member.id,
            'name': member.name,
            'tags': tags_list,
        })

    list_json = json.dumps(result_list)
    context = {'list_json': list_json}
    return render(request, 'index.html', context)