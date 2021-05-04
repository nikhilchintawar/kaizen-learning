from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=200)
    description = RichTextField()
    summary = RichTextField()
    is_free = models.BooleanField(default=False)
    is_purchased = models.BooleanField(default=False)
    price = models.IntegerField()
    banner = models.ImageField(upload_to="static/courses/banners/%Y/%m")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
