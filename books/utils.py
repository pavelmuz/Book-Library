from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Book


def paginate_books(request, books_list, results):
    page = request.GET.get('page')
    paginator = Paginator(books_list, results)

    try:
        books_list = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        books_list = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        books_list = paginator.page(page)

    left_index = int(page) - 4

    if left_index < 1:
        left_index = 1

    right_index = int(page) + 5

    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    return custom_range, books_list


def search_books(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    books_list = Book.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(author__icontains=search_query)
    )

    return books_list, search_query
