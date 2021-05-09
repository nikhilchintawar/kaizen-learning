from django.urls import path, include
from rest_framework import routers

from api.courses.views.courses import CoursesViewset

app_name="courses"
router = routers.DefaultRouter()
router.register(r'', CoursesViewset,  basename='courses')

urlpatterns = [
    path('', include(router.urls))
]