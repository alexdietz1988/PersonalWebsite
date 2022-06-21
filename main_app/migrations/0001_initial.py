# Generated by Django 4.0.5 on 2022-06-21 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('text', models.TextField(max_length=10000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tags', models.ManyToManyField(related_name='posts', to='main_app.tag')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
