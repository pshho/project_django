from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('post/create/', views.post_create, name='post_create'),
    path('category/<str:slug>/', views.category_page, name='category_page'),
    path('delete/<int:post_id>/', views.post_delete, name='post_delete'),
    path('comment/create/<int:post_id>/', views.comment_create, name='comment_create'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('comment/update/<int:comment_id>/', views.comment_update, name='comment_update'),
]