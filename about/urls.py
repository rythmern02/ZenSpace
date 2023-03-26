from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('learnm',views.learnm, name='learnm')
 
]