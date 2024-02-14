from django.urls import path
from . import views

app_name = 'lab2'

urlpatterns = [
    path('', views.home_view, name="home"),
    path('send', views.send_message, name="send"),
    path('inbox', views.view_messages, name="inbox"),
]