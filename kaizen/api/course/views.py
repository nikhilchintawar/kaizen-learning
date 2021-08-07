from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.course.serializers import CoursesSerializer
from api.course.models import Courses


class CoursesPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"


class CoursesViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CoursesPagination
    serializer_class = CoursesSerializer
    lookup_field = "url"
    slug_from = "url"
    slug = "url"
    queryset = Courses.objects.all()
