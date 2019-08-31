from rest_framework_nested import routers
from schools.views.school_view import SchoolViewSet
from students.views.students_view import StudentViewSet
from django.conf.urls import url
from django.urls import include, path

router = routers.SimpleRouter()
router.register(r'schools', SchoolViewSet)
schools_router = routers.NestedSimpleRouter(router, r'schools', lookup='id')
schools_router.register(r'students', StudentViewSet, base_name='students')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(schools_router.urls)),
  ]

