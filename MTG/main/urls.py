from django.urls import path
from . import views

urlpatterns =[
    path(r'',views.blank,name='blank'),
    path(r'home/',views.home,name='home'),
]
