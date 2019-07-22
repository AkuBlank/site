from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), #при пустом url будет отображаться post_lits
    path('post/<int:pk>', views.post_detail, name='post_detail'), #при /post/№ будет детально отображаться пост под номером
    path('post/new/', views.post_new, name='post_new'), #при /post/new будет открываться создание поста
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'), #при /post/№/edit будет редактироваться пост под номером

]
