from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app1-home'),
    path('profile/', views.profile, name='app1-profile'),
    path('friends/', views.friends, name='app1-friends'),
]
