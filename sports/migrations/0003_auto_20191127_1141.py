# Generated by Django 2.2.3 on 2019-11-27 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0002_auto_20191017_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(max_length=500)),
                ('team1', models.CharField(max_length=100)),
                ('team2', models.CharField(max_length=100)),
                ('logo1', models.ImageField(upload_to='isl')),
                ('logo2', models.ImageField(upload_to='isl')),
            ],
        ),
        migrations.AlterField(
            model_name='sports',
            name='img',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
