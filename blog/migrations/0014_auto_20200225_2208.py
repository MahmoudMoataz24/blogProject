# Generated by Django 3.0.3 on 2020-02-25 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200225_2208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AlterField(
            model_name='post',
            name='tagName',
            field=models.CharField(default='null', max_length=30),
        ),
    ]
