# Generated by Django 3.0.1 on 2021-08-31 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0015_auto_20210825_0943'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=200)),
                ('timer', models.PositiveIntegerField()),
                ('ans', models.BooleanField()),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='robot.Time')),
            ],
        ),
    ]