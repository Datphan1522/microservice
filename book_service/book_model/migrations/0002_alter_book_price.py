# Generated by Django 4.1.6 on 2023-03-28 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_model', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.CharField(max_length=15),
        ),
    ]
