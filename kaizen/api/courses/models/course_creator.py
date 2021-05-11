from django.db import models

from .courses import Courses
from api.author.models import Author


class Course_Creator(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.PROTECT)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="course_creator") #related name should be the same as model class name in lowercase

    def __str__(self):
        return f"{self.course}-{self.authors}"
