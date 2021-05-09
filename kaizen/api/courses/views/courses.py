from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.courses.serializers.courses import CoursesSerializer
from api.courses.models.courses import Courses


class CoursesPagination(PageNumberPagination):
    page_size=10
    page_size_query_param='page_size'

class CoursesViewset(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    pagination_class = CoursesPagination
    serializer_class=CoursesSerializer
    lookup_field = "url"
    slug_from = "url"
    queryset = Courses.objects.all()

