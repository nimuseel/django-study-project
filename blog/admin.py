from django.contrib import admin
from .models import Post

# 관리자 페이지에서 만든 모델을 보려면 아래 코드로 모델을 등록해야 한다.
admin.site.register(Post)