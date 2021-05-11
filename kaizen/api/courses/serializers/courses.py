from rest_framework import serializers

from api.courses.models.courses import Courses
from api.courses.serializers.course_creator import CourseCreatorSerializer
from api.courses.serializers.course_lessons import CourseLessonsSerializer
from api.lesson.models import Lesson
class CoursesSerializer(serializers.ModelSerializer):
    course_url = serializers.HyperlinkedIdentityField(view_name='courses:courses-detail', lookup_field='url')
    banner = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=True, required=False)
    course_lessons = CourseLessonsSerializer(many=True, source="course_lessons_set")
    course_creator = CourseCreatorSerializer(many=True, source="course_creator_set")


    class Meta:
        model=Courses
        fields=[
            "id",
            "name",
            "description",
            "summary",
            "url",
            "is_free",
            "is_purchased",
            "price",
            "banner",
            "created_at",
            "updated_at",
            "course_url",
            'course_lessons',
            'course_creator',
            ]
        # additional_fields=[ 'authors']