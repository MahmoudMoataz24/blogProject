# Generated by Django 3.0.3 on 2020-02-25 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20200225_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='likes',
            name='likes',
            field=models.BooleanField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=2, upload_to=''),
            preserve_default=False,
        ),
    ]
