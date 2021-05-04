# Generated by Django 3.2 on 2021-05-04 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("lesson", "0001_initial"),
        ("author", "0001_initial"),
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Course_Lessons",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="courses.courses",
                    ),
                ),
                (
                    "lessons",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lesson.lesson",
                        verbose_name="Course Lessons",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Course_Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "authors",
                    models.ManyToManyField(
                        to="author.Author", verbose_name="Course Authors"
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="courses.courses",
                    ),
                ),
            ],
        ),
    ]