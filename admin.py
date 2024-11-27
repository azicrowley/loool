from django.contrib.auth.models import User  # Импорт модели User
from .models import News
from django.contrib import admin

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'author_name')  # Используем author_name

    def author_name(self, obj):
        return obj.author.username  # Возвращаем имя пользователя или другое поле из модели User
    author_name.admin_order_field = 'author'  # Опционально: сортировка по полю author
    author_name.short_description = 'Автор'  # Отображаемое имя в админке

admin.site.register(News, NewsAdmin)







