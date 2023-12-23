from django.urls import path
from . import views


urlpatterns = [
    path('', views.books_view, name='books'),
    path('add-book', views.add_book_view, name='add-book'),
    path('about', views.about_view, name='about')
]
