from django.urls import path
from . import views


app_name = 'base_app'
urlpatterns = [
    path('', views.welcome, name='welcome'),
]
