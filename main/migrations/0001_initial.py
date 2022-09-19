# Generated by Django 4.1.1 on 2022-09-19 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('producer', models.CharField(max_length=50)),
                ('rate', models.PositiveIntegerField(default=0, max_length=10, verbose_name='Рейтинг')),
                ('duration', models.DurationField(verbose_name='Продолжительность')),
            ],
        ),
    ]