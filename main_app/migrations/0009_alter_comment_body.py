# Generated by Django 4.0.5 on 2022-06-29 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
