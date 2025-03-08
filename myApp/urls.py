from django.urls import path
from . import views  # Import views correctly

urlpatterns = [
   path('about/', views.about),
   path('index/', views.index),
   path('agents/', views.agents),
   path('contact/', views.contact),
   path('properties/', views.properties),
   path('property_single/', views.property_single),
   path('service_details/', views.service_details),
   path('services/', views.services),
   path('starter_page/', views.starter_page),
   path('signup/', views.signup,),
   path('loginpage/', views.loginpage,),

]