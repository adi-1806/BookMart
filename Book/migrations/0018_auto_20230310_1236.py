# Generated by Django 3.2.17 on 2023-03-10 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0017_alter_books_user_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='books_library',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='books_store',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
