# Generated by Django 3.2.17 on 2023-03-03 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0004_auto_20230228_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='books_library',
            name='image',
            field=models.FileField(null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='books_store',
            name='image',
            field=models.FileField(null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='books_user',
            name='image',
            field=models.FileField(null=True, upload_to='images'),
        ),
    ]