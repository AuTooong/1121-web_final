# Generated by Django 3.2.21 on 2023-12-31 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=100)),
                ('ext', models.IntegerField()),
            ],
        ),
    ]