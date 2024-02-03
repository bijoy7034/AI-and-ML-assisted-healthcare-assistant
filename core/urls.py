from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [

path('', views.home, name='home'),
path('register/', views.registerView, name='reg'),
path('reg_user/', views.registerUser, name='reg_user'),
path('login/', views.loginView, name='login'),
path('patient/', views.patient_home, name='patient'),
path('create_profile/', views.create_profile, name='create_profile'),
path('diagnosis/', views.diagnosis, name='diagnosis'),
path('diagnosis/predict', views.MakePredict, name='predict'),
path("location/", views.locationServices, name="location"),
path('result/', views.patient_result, name='result'),
path('profile/', views.profile_details, name="profile"),    
path('result/ment', views.MakeMent, name='ment'),
path('ment/', views.patient_ment, name='ment_list'),
path('logout/', views.logoutView, name='logout'),
]
