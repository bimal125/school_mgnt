from students.views.students_view import StudentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', StudentViewSet, basename='student')
urlpatterns = router.urls