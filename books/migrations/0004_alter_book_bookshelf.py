# Generated by Django 5.0 on 2023-12-23 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_description_alter_book_bookshelf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookshelf',
            field=models.CharField(choices=[('Шкаф №1', 'Шкаф №1'), ('Шкаф №2', 'Шкаф №2'), ('Полки', 'Полки')], max_length=100),
        ),
    ]
