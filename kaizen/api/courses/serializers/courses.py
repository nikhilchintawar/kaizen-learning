from rest_framework import serializers

from api.courses.models.courses import Courses
from api.courses.serializers.course_creator import CourseCreatorSerializer
from api.courses.serializers.course_lessons import CourseLessonsSerializer

class CoursesSerializer(serializers.ModelSerializer):
    banner = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=True, required=False)
    lessons = CourseLessonsSerializer(many=True)
    authors = CourseCreatorSerializer(many=True)

    class Meta:
        model=Courses
        fields=["id", "name", "description", "summary", "is_free", "is_purchased", "price", "banner", "created_at", "updated_at"]
        additional_fields=['lessons', 'authors']