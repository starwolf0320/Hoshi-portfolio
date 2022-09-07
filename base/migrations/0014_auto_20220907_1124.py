# Generated by Django 3.0.8 on 2022-09-07 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_auto_20201109_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='/images/placeholder.png', null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='/user.png', null=True, upload_to='images'),
        ),
    ]
