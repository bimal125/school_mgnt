from schools.views.school_view import SchoolViewSet
from rest_framework.routers import DefaultRouter
from schools.views.school_view import ListSchool
from django.urls import path

router = DefaultRouter()
router.register(r'', SchoolViewSet, basename='school')
urlpatterns = router.urls

urlpatterns = [
      path('list/', ListSchool.as_view()),
]+urlpatterns