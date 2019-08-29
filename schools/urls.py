from schools.views.school_view import SchoolViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', SchoolViewSet, basename='school')
urlpatterns = router.urls