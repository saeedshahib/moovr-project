# Generated by Django 3.1 on 2020-08-26 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_auto_20200826_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='DateAdded',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
