# Generated by Django 5.0.6 on 2024-05-22 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0012_remove_book_is_borrowed_borrowedbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_borrowed',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='BorrowedBook',
        ),
    ]
