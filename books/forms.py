from django.forms import ModelForm
from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description',
                  'bookshelf', 'shelf', 'placement']

        labels = {
            'title': 'Название:',
            'author': 'Автор:',
            'description': 'Описание:',
            'bookshelf': 'Шкаф:',
            'shelf': 'Полка:',
            'placement': 'Расположение на полке:'
        }

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control my-2'
            })
