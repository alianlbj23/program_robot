# Generated by Django 3.0.1 on 2021-08-25 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0014_auto_20210825_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store_point',
            name='time',
            field=models.PositiveIntegerField(),
        ),
    ]