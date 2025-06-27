from django.db import models

# 태그 모델 정의
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)  # 태그 이름
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# 걸그룹 멤버 모델 정의
class Member(models.Model):
    name = models.CharField(max_length=100)  # 멤버 이름
    tags = models.ManyToManyField(Tag, related_name="members")  # 멤버와 태그는 다대다 관계

    def __str__(self):
        return f'{self.name} ({', '.join([tag.name for tag in self.tags.all()])})'