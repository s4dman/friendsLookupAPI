# Generated by Django 3.0.4 on 2020-03-15 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Friend',
            new_name='Friends',
        ),
    ]
