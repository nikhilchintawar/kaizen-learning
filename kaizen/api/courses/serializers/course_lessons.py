from rest_framework import fields, serializers

from api.courses.models.course_lessons import Course_Lessons
from api.lesson.serializers import LessonSerializer

class CourseLessonsSerializer(serializers.ModelSerializer):
    lesson=LessonSerializer()
    class Meta:
        model= Course_Lessons
        fields=['lesson']