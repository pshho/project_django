"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from board import views

app_name = 'board'

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('<int:question_id>', views.detail, name='detail'),
    path('question/create/', views.question_create, name='question_create'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
]
