from django.db import models

from .courses import Courses
from api.author.models import Author


class Course_Author(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.PROTECT)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE, db_index=True)

    def __str__(self):
        return f"{self.course}-{self.authors}"
