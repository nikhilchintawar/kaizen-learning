from django.db import models

from ckeditor.fields import RichTextField

from api.lesson.models import Lesson
from api.author.models import Author

# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=200)
    description = RichTextField()
    summary = RichTextField()
    url = models.CharField(max_length=100, default="null")
    is_free = models.BooleanField(default=False)
    is_purchased = models.BooleanField(default=False)
    price = models.IntegerField()
    banner = models.ImageField(upload_to="static/courses/banners/%Y/%m")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Course_Authors(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.PROTECT)
    authors = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="course_authors"
    )  # related name should be the same as model class name in lowercase

    def __str__(self):
        return f"{self.course}-{self.authors}"


class Course_Lessons(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    lessons = models.OneToOneField(
        Lesson,
        verbose_name=("Course Lessons"),
        on_delete=models.CASCADE,
        related_name="course_lessons",
    )

    def __str__(self):
        return f"{self.course}-{self.lessons}"
