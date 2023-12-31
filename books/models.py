import uuid
from django.db import models
from users.models import Profile

# Create your models here.


class Book(models.Model):
    BOOKSHELF_TYPE = (
        ('Шкаф №1', 'Шкаф №1'),
        ('Шкаф №2', 'Шкаф №2'),
        ('Полки', 'Полки')
    )
    owner = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    bookshelf = models.CharField(max_length=100, choices=BOOKSHELF_TYPE)
    shelf = models.IntegerField()
    placement = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering: ['title', 'author']
