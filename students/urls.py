from students.views.students_view import StudentViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')
urlpatterns = router.urls