form django.urls import path
form . import views

urldpatterns = [
    path('', views.post_list, name="post_list'),
]