from django.db import models

from .courses import Courses
from api.lesson.models import Lesson


class Course_Lessons(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    lessons = models.OneToOneField(
        Lesson, verbose_name=("Course Lessons"), on_delete=models.CASCADE, related_name="course_lessons"
    )

    def __str__(self):
        return f"{self.course}-{self.lessons}"
