# Generated by Django 3.1.2 on 2020-11-01 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeer', '0004_auto_20201101_0335'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeer',
            name='mobile',
            field=models.IntegerField(max_length=10, null=True, unique=True),
        ),
    ]