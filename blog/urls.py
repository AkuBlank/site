from django.urls import path
from . import views

urldpatterns = [
    path('', views.post_list, name="post_list'),
]