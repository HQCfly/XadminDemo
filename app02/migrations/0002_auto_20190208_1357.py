# Generated by Django 2.1.1 on 2019-02-08 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='Foodeat',
        ),
        migrations.RenameModel(
            old_name='Food',
            new_name='Transactions',
        ),
    ]