# Generated by Django 3.2.17 on 2023-03-09 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0016_remove_books_user_look'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books_user',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
