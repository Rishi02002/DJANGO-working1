from django.urls import path
from .import views

urlpatterns=[
    
   
    path('', views.index, name='index'),
    
     path('index', views.index, name='index'),

    path('register', views.register, name='register'),

    path('news', views.news, name='news'),

    path('login', views.login, name='login'),

    path('about', views.about, name='about'),

    path('logout', views.logout, name='logout'),

  
    
 
]