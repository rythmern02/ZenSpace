from django.urls import path
from . import views

urlpatterns = [
    path('club_detail/',views.club_detail, name='club_detail'),
    path('create/', views.create_club_view, name='create_club'),
    path('<int:club_id>/join/', views.join_club_view, name='join_club'),
    path('club_list/', views.club_list ,name='club_list'),
    path('clubs', views.clubs, name='clubs')
    
    
]

