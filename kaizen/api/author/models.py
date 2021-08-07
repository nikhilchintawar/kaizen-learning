from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    bio = RichTextField()
    profile_image = models.ImageField(upload_to="static/author/profile/%Y/%m")
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
