from django.urls import path
from . import views


urlpatterns = [
    path('', views.boots_app, name='boots'),
    path('football_form/<str:slug>/', views.football_form_detail, name='football_form_detail'),
    path('boots/<str:slug>/', views.boots_detail, name='boots_detail'),
    path('goalkeeper_form/<str:slug>/', views.goalkeeper_form_detail, name='goalkeeper_form_detail'),
    path('football_form/', views.football_form_app, name='football_form'),
    path('goalkeeper_form/', views.goalkeeper_form_app, name='goalkeeper_form'),
]