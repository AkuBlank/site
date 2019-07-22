from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model): #создали модель поста
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #здесь пример того как идентифицировать юзера
    title = models.CharField("Заголовок:", max_length=200) #CharField для небольших строк
    text = models.TextField("Текст:") #TextField для текста без ограничений
    created_date = models.DateTimeField(default=timezone.now) #DateTimeField для времени
    published_date = models.DateTimeField(blank=True, null=True) #можно выставить дату публикации

    def publish(self): #функция "публикации"
        self.published_date = timezone.now() #ставится время публикации
        self.save() #сохраняются изменения

    def __str__(self): #это обязательная вещь
        return self.title #нет, серьезно, без этого нельзя
