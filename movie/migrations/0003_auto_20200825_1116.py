# Generated by Django 3.1 on 2020-08-25 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_movie_dateadded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='DateAdded',
            field=models.TimeField(),
        ),
    ]