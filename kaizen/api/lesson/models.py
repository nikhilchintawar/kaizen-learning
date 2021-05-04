from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.
class Lesson(models.Model):
    title = models.CharField(max_length=250)
    summary = RichTextField()
    theory = RichTextField()
    video_link = models.CharField(max_length=300)
