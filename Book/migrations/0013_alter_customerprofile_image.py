# Generated by Django 3.2.17 on 2023-03-07 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0012_alter_customerprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='image',
            field=models.ImageField(null=True, upload_to='profiles'),
        ),
    ]
