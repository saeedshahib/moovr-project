# Generated by Django 3.1 on 2020-08-25 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20200825_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='DateAdded',
            field=models.DateTimeField(),
        ),
    ]
