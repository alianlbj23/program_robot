# Generated by Django 3.0.1 on 2021-08-18 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0011_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='sort_term_memory',
            name='number',
            field=models.CharField(default=12, max_length=10),
            preserve_default=False,
        ),
    ]