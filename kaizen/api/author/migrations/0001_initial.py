# Generated by Django 3.2 on 2021-08-06 03:08

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('bio', ckeditor.fields.RichTextField()),
                ('profile_image', models.ImageField(upload_to='static/author/profile/%Y/%m')),
                ('joined_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
