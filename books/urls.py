from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('books/', views.books_view, name='books'),
    path('add-book/', views.add_book_view, name='add-book'),
    path('book/<str:pk>/', views.book_view, name='book'),
    path('delete-book/<str:pk>/', views.delete_book_view, name='delete-book'),
    path('update-book/<str:pk>/', views.update_book, name='update-book')
]
