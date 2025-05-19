from django.urls import path
from . import views

app_name = 'manga'  

urlpatterns = [
    path('list.html', views.manga_list, name='list'),
    path('<slug:slug>/', views.manga_detail, name='detail'),
    path('<slug:slug>/chapter/<int:chapter_number>/', views.chapter_view, name='chapter_view'), 
]