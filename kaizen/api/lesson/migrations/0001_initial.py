# Generated by Django 3.2 on 2021-05-04 02:39

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('summary', ckeditor.fields.RichTextField()),
                ('theory', ckeditor.fields.RichTextField()),
                ('video_link', models.CharField(max_length=300)),
            ],
        ),
    ]
