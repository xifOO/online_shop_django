from django.urls import path
from . import views


urlpatterns = [
    path('search', views.Search.as_view(), name='search'),
]