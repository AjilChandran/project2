# Generated by Django 2.2.3 on 2019-10-17 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sports',
            name='date',
            field=models.DateField(auto_now_add=True, default='1992-11-1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sports',
            name='head',
            field=models.CharField(default='bigileeee', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sports',
            name='img',
            field=models.ImageField(default='img.jpg', upload_to='static/images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sports',
            name='sub',
            field=models.CharField(default='poonkai sasi', max_length=10000),
            preserve_default=False,
        ),
    ]