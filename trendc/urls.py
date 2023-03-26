from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('trending_programming_courses',views.trending_programming_courses, name='trending_programming_courses'),
    path('trending_music_courses',views.trending_music_courses, name='trending_music_courses'),
    path('trending_education_courses',views.trending_education_courses, name='trending_education_courses'),
    
]
