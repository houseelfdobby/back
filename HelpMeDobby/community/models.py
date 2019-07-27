from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User # 임시
from django.conf import settings

# Create your models here.

# 게시판 리스트
table = ['자유','빈방','맛집','프리마켓']

def category_check(data):
    if data not in table:
        raise ValidationError(
            ('The value is not valid. => %(data)s'),
            params={'data': data},
        )

class Post(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()
    category = models.CharField(max_length=20, validators=[category_check])
    publish_date = models.DateTimeField(auto_now_add=True) # 생성일자
    edit_date = models.DateTimeField(auto_now=True) # 수정일자


    # 내용에 들어갈 이미지도 들어가야함
    def __str__(self):
        return self.title