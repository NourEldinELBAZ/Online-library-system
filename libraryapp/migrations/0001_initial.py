# Generated by Django 5.0.6 on 2024-05-13 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('author', models.CharField(max_length=75)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=50)),
                ('cover', models.ImageField(upload_to='')),
            ],
        ),
    ]
