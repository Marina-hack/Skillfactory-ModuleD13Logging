from django.contrib import admin
from .models import Category, Post, PostCategory

# напишем уже знакомую нам функцию обнуления товара на складе
def nullfy_quantity(modeladmin, request, queryset):
    # все аргументы уже должны быть вам знакомы, самые нужные из них это request — объект хранящий информацию о запросе и queryset — грубо говоря набор объектов, которых мы выделили галочками.
    queryset.update(quantity=0)
    nullfy_quantity.short_description = 'Обнулить'  # описание для более понятного представления в админ панеле задаётся, как будто это объект


# создаём новый класс для представления  в админке
class PostAdmin(admin.ModelAdmin):
#     # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('author', 'type_post', 'rating_post')  # оставляем только имя и цену товара
    list_filter = ('type_post', 'author', 'category', 'rating_post', 'title_post')  # добавляем примитивные фильтры в нашу админку
    search_fields = ('title_post', 'category__name')  # тут всё очень похоже на фильтры из запросов в базу
    actions = [nullfy_quantity]  # добавляем действия в список

# Register your models here.


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
