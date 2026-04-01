from django.urls import path
from . import views

urlpatterns = [

    path('', views.home_view, name='home'),
    path('contactus', views.contactus_view, name='contactus'),

]