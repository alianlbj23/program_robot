# Generated by Django 3.2.3 on 2021-08-04 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0007_auto_20210803_1503'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterField(
            model_name='userdata',
            name='image',
            field=models.ImageField(upload_to='headshot/'),
        ),
    ]
