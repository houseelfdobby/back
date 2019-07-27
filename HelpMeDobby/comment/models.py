from django.db import models
from community.models import Post
# Create your models here.


class Comment(models.Model):
    # user = models.ForeignKey("app.Model", on_delete=models.CASCADE) 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments') # 게시글과 1:N 관계
    content = models.CharField(max_length=500) # 내용
    publish_date = models.DateTimeField(auto_now_add=True) # 생성일자
    edit_date = models.DateTimeField(auto_now=True) # 수정일자

    def __str__(self):
        return self.content[:10]
    