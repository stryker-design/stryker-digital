# Generated by Django 4.1.4 on 2022-12-17 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blogpost_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]