from rest_framework import serializers

from api.course.models import Courses
from api.course.models import Course_Lessons
from api.lesson.serializers import LessonSerializer
from api.author.serializers import AuthorSerializer
from api.course.models import Course_Authors


class CourseLessonsSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer()

    class Meta:
        model = Course_Lessons
        fields = ["lessons"]


class CourseAuthorsSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer()

    class Meta:
        model = Course_Authors
        fields = ["authors"]


class CoursesSerializer(serializers.ModelSerializer):
    course_url = serializers.HyperlinkedIdentityField(
        view_name="course:course-detail", lookup_field="url"
    )
    banner = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False
    )
    course_lessons = CourseLessonsSerializer(many=True, source="course_lessons_set")
    course_authors = CourseAuthorsSerializer(many=True, source="course_authors_set")

    class Meta:
        model = Courses
        fields = [
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
            "course_lessons",
            "course_authors",
        ]
        # additional_fields=[ 'authors']

    # def create(self, validated_data):
    # course= Courses.objects.create(**validated_data)
    # course_lessons_set_serializer = self.fields['course_lessons']
    # authors_set_serializer = self.fields['course_creator']
    # return course
