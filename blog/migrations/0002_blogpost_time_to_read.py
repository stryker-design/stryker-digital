# Generated by Django 4.1.4 on 2022-12-17 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='time_to_read',
            field=models.CharField(default='5', max_length=10),
        ),
    ]
