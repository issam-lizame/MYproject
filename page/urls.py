from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Member', views.member, name='member'),
    path('courses', views.courses, name='courses'),
]