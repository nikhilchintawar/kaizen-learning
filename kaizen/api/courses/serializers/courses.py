from rest_framework import serializers

from api.courses.models.courses import Courses
from api.courses.serializers.course_creator import CourseCreatorSerializer
from api.courses.serializers.course_lessons import CourseLessonsSerializer
from api.lesson.models import Lesson
class CoursesSerializer(serializers.ModelSerializer):
    course_url = serializers.HyperlinkedIdentityField(view_name='courses:courses-detail', lookup_field='url')
    banner = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=True, required=False)
    # lessons = CourseLessonsSerializer(many=True, write_only=True)
    # authors = CourseCreatorSerializer(many=True, read_only=True)
    # lesson_id = serializers.PrimaryKeyRelatedField(queryset=Lesson.objects.all(), source='lessons', write_only=True)

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
            # 'lessons',
            # 'authors',
            # "lesson_id"
            ]
        # additional_fields=["course_url", 'lessons', 'authors']