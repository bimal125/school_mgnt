from students.views.student_view import StudentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', StudentViewSet, basename='student')
urlpatterns = router.urls