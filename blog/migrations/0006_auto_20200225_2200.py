# Generated by Django 3.0.3 on 2020-02-25 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200225_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='likes',
            field=models.BooleanField(default='null', null=True),
        ),
    ]
