# Generated by Django 4.1.4 on 2022-12-17 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_time_to_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.CharField(default='Andy Walker', max_length=255),
        ),
    ]
