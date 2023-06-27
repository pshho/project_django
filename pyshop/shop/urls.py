from django.contrib import admin
from django.urls import path, re_path

from shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_in_category, name='product_all'),
    re_path(r'^(?P<category_slug>[-\w]+)/$', views.product_in_category, name='product_in_category'),
    path('<int:id>/<product_slug>/', views.product_detail, name='product_detail'),
]