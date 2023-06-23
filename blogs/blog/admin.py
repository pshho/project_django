from django.contrib import admin
from .models import Post, Category

admin.site.register(Post)

# 카테고리 등록
class CategoryAdmin(admin.ModelAdmin):
    # slug와 name이 동시에 입력됨
    prepopulated_fields = {'slug':('name', )}   # name 튜플

admin.site.register(Category, CategoryAdmin)
