# Generated by Django 2.1.4 on 2019-03-07 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FoodApp', '0002_delete_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Email',
            new_name='Subscribe',
        ),
    ]
