# Generated by Django 4.1 on 2022-09-08 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_remove_registration_phone'),
    ]

    operations = [
        migrations.DeleteModel(
            name='registration',
        ),
        migrations.DeleteModel(
            name='Todolist',
        ),
    ]
