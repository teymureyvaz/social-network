# Generated by Django 3.2.8 on 2021-10-11 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20211011_2002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes_count',
        ),
    ]
