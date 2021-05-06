from rest_framework import fields, serializers
from .models import Lesson

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lesson
        fields=['id', 'title', 'summary', 'theory', 'video_link']
