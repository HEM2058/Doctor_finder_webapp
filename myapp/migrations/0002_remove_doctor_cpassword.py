# Generated by Django 4.1.4 on 2022-12-09 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='cpassword',
        ),
    ]
