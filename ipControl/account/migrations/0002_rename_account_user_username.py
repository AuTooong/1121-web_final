# Generated by Django 3.2.21 on 2023-12-31 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='account',
            new_name='username',
        ),
    ]
