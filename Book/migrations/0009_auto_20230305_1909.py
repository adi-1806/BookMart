# Generated by Django 3.2.17 on 2023-03-05 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0008_auto_20230305_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookstoreprofile',
            name='image',
            field=models.FileField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='image',
            field=models.FileField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='libraryprofile',
            name='image',
            field=models.FileField(null=True, upload_to='images'),
        ),
    ]
