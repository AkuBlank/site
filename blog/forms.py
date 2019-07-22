from django import forms
from .models import Post

class PostForm(forms.ModelForm): #создали тип формы

    class Meta: #хз почему, но так надо
        model = Post #какую модель создаем
        fields = ('title', 'text',) #поля которые заполняются
