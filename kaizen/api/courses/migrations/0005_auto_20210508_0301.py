# Generated by Django 3.2 on 2021-05-08 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='url',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.DeleteModel(
            name='Course_Author',
        ),
    ]
