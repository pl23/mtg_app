from django.urls import path
from . import views

urlpatterns =[
    path(r'',views.blank,name='blank'),
    path(r'home/',views.home,name='home'),
    path(route=r'login/', view=views.login),
    path(route=r'register/', view=views.register),
]
