from django.urls import path
from . import views


urlpatterns = [
    path('feedbacks', views.feedback, name='feedbacks'),
    path('mailing', views.mailing, name='mailing'),
]