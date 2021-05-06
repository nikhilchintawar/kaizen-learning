from rest_framework import fields, serializers

from api.author.serializers import AuthorSerializer
from api.courses.models.course_creator import Course_Creator

class CourseCreatorSerializer(serializers.ModelSerializer):
    author=AuthorSerializer()

    class Meta:
        model=Course_Creator
        fields=['author']