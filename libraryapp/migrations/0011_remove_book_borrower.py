# Generated by Django 5.0.6 on 2024-05-22 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0010_alter_book_options_alter_book_borrower'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='borrower',
        ),
    ]
