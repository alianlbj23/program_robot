# Generated by Django 3.0.1 on 2021-09-08 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0023_auto_20210908_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamedata',
            name='five',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='gamedata',
            name='four',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='gamedata',
            name='one',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='gamedata',
            name='three',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='gamedata',
            name='two',
            field=models.BooleanField(),
        ),
    ]
