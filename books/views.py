from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm
from .utils import search_books, paginate_books

# Create your views here.


@login_required(login_url='login')
def books_view(request):
    books_list, search_query = search_books(request)

    custom_range, books_list = paginate_books(request, books_list, 3)

    context = {
        'books': books_list,
        'search_query': search_query,
        'custom_range': custom_range
    }
    return render(request, 'books/books.html', context)


@login_required(login_url='login')
def book_view(request, pk):
    book = Book.objects.get(id=pk)
    context = {'book': book}
    return render(request, 'books/book.html', context)


@login_required(login_url='login')
def add_book_view(request):
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')

    context = {'form': form}
    return render(request, 'books/book-form.html', context)


@login_required(login_url='login')
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


@login_required(login_url='login')
def delete_book_view(request, pk):
    book = Book.objects.get(id=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('books')

    context = {'book': book}
    return render(request, 'books/delete-book.html', context)


def home_view(request):
    return render(request, 'books/home.html')
