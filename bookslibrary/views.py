from django.shortcuts import render


def page_not_found(request, exception):
    return render(request, 'error-view.html', status=404)
