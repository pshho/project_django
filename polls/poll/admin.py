from django.contrib import admin
from poll.models import Question, Choice, Seoulestate

# Question, Choice 클래스 관리자 페이지에 등록
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Seoulestate)
