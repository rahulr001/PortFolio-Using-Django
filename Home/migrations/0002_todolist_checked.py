# Generated by Django 4.1 on 2022-08-14 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='checked',
            field=models.BooleanField(default=False),
        ),
    ]