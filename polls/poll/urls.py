from django.core.files import temp
from django.urls import path
from django.views.generic import TemplateView

from . import views

# name space(이름 공간)
app_name = 'poll'

urlpatterns = [
    path("", views.index, name="index"),
    # http://127.0.0.1:8000/poll/
    path("poll_list", views.poll_list, name="poll_list"),
    # http://127.0.0.1:8000/poll/test
    path("test/", views.test, name="test"),
    # http://127.0.0.1:8000/poll/
    path("<int:question_id>", views.detail, name="detail"),
    path("<int:question_id>/vote", views.vote, name="vote"),
    path("search/", views.search, name="search"),
    path("search2/", views.search2, name="search2"),
    path('calendar/', views.calendar, name='calendar'),
    path('calendar/calendar_iframe/<str:title>/', views.calendar_iframe, name='calendar_iframe'),
    path('map_convert/', views.map_convert, name='map_convert'),
    path('search_map.js', TemplateView.as_view(template_name='search_map.js', content_type='application/javascript'), name='search_map'),
]