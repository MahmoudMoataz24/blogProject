# Generated by Django 3.0.3 on 2020-02-25 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='likes',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=2, upload_to=''),
            preserve_default=False,
        ),
    ]
