# Generated by Django 5.0 on 2023-12-23 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='titile',
            new_name='title',
        ),
    ]
