from schools.serializers.SchoolSerializer import SchoolSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from schools.models import School
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
class SchoolViewSet(viewsets.ModelViewSet):
    """
    A viewset for schools.
    """
    serializer_class = SchoolSerializer
    queryset = School.objects.all()
    lookup_field = 'id'
    filter_backends = (DjangoFilterBackend, OrderingFilter, )
    filter_fields = ("name","max_students",)
    ordering_fields = ("max_students",)

