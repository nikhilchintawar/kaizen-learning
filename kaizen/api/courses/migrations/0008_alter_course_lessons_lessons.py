# Generated by Django 3.2 on 2021-05-10 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0001_initial'),
        ('courses', '0007_remove_courses_lessons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_lessons',
            name='lessons',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='course_lessons', to='lesson.lesson', verbose_name='Course Lessons'),
        ),
    ]
