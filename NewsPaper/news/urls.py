from django.urls import path
# Импортируем созданное нами представление
from .views import (BreakingNews, News, Articles, PostCreate, PostDelete, PostUpdate, subscriptions, IndexView)
from django.urls import path
from django.views.decorators.cache import cache_page


urlpatterns = [
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
    path('index/', IndexView.as_view()),
    path('', cache_page(60*1)(News.as_view()), name='news'),
    path('<int:pk>', cache_page(60*1)(BreakingNews.as_view()), name='post_detail'),
    path('articles/<int:pk>', cache_page(60*1)(Articles.as_view())),
    # path('search/', NewsSearch.as_view(), name='search'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('subscriptions/', subscriptions, name='subscriptions'),
    # path('subscriptions/', CategoryListView.as_view(), name='subscriptions')
]


# pk — это первичный ключ товара, который будет выводиться у нас в шаблон
# int — указывает на то, что принимаются только целочисленные значения
