from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

# Create your views here.


def books_view(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books/books.html', context)


def book_view(request, pk):
    book = Book.objects.get(id=pk)
    context = {'book': book}
    return render(request, 'books/book.html', context)


def add_book_view(request):
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')

    context = {'form': form}
    return render(request, 'books/book-form.html', context)


def update_book(request, pk):
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books')

    context = {'form': form}
    return render(request, 'books/book-form.html', context)


def delete_book_view(request, pk):
    book = Book.objects.get(id=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('books')

    context = {'book': book}
    return render(request, 'books/delete-book.html', context)


def about_view(request):
    return render(request, 'books/about.html')
