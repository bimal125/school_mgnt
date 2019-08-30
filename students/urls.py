from students.views.students_view import StudentViewSet
from rest_framework.routers import DefaultRouter
from students.views.students_view import ListStudent
from django.urls import path

router = DefaultRouter()
router.register(r'', StudentViewSet, basename='student')
urlpatterns = router.urls

urlpatterns = [
      path('list/', ListStudent.as_view()),
]+urlpatterns