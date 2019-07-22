from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

def post_list(request): #request обязателен везде во views.py
    posts = Post.objects.all().order_by('-published_date') #выводим все посты и сортируем по дате (можно написать [:4] чтобы отображались 4 последних поста)
    return render(request, 'blog/post_list.html', {'posts': posts}) #показываем все посты через шаблон html

def post_detail(request, pk): #здесь pk счетчик постов
    post = get_object_or_404(Post, pk=pk) #либо выдает пост, либо ошибку
    return render(request, 'blog/post_detail.html', {'post': post}) #показываем пост через шаблон html

def post_new(request):
    if request.method == "POST": #проверяет отправляет ли пользователь что-то на сервер (противоположность GET)
        form = PostForm(request.POST) #открывает форму если правда
        if form.is_valid(): #написано ли что-то в полях
            post = form.save(commit=False) #сохраняет без комментиариев
            post.author = request.user #определяет юзера
            post.published_date = timezone.now() #выставляет дату на СЕЙЧАС
            post.save() #сохраняет пост
            return redirect('post_detail', pk=post.pk) #направляет на post_detail конкретного поста(см выше)
    else:
        form = PostForm() #хз честно
    return render(request, 'blog/post_edit.html', {'form': form}) #показывает саму страницу редактирования

def post_edit(request, pk): #аналогично функции выше, но поле изначально заполнено постом (instance)
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
