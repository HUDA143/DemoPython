# Generated by Django 3.2.14 on 2022-07-17 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1994-06-23'),
            preserve_default=False,
        ),
    ]
