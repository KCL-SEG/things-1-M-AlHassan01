# Generated by Django 4.2.7 on 2023-11-29 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Things',
            new_name='Thing',
        ),
    ]
