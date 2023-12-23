from django.shortcuts import render
from .models import Book

# Create your views here.


def books_view(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books/books.html', context)


def add_book_view(request):
    return render(request, 'books/add-book.html')


def about_view(request):
    return render(request, 'books/about.html')
