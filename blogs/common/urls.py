from django.urls import path
from django.contrib.auth import views as auth_views

from common import views

app_name = 'common'

urlpatterns = [
    # 클래스형 LoingView 사용
    path('login/', auth_views.LoginView.as_view(
        template_name = 'common/login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # 함수형 view 제작 및 사용
    path('signup/', views.signup, name='signup'),
]