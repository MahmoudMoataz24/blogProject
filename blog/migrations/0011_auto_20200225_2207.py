# Generated by Django 3.0.3 on 2020-02-25 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200225_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='likes',
            field=models.BooleanField(default=2),
            preserve_default=False,
        ),
    ]
