# Generated by Django 4.0.5 on 2022-06-23 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_post_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
    ]
