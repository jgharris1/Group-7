# Generated by Django 3.2.12 on 2022-02-19 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='poster',
            new_name='user',
        ),
    ]
