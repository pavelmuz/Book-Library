from django.forms import ModelForm
from django import forms
from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

        labels = {
            'title': 'Название:',
            'author': 'Автор:',
            'description': 'Описание:',
            'bookshelf': 'Шкаф:',
            'shelf': 'Полка:'
        }

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control my-2'
            })
