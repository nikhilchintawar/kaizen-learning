from django.urls import path, include
from rest_framework import routers

from api.course.views import CoursesViewset

app_name = "course"
router = routers.DefaultRouter()
router.register(r"", CoursesViewset, basename="course")

urlpatterns = [path("", include(router.urls))]
