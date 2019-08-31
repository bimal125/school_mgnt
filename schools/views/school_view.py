from schools.serializers.SchoolSerializer import SchoolSerializer
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from schools.models import School
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework import generics
from rest_framework import filters

class SchoolViewSet(viewsets.ModelViewSet):
    """
    School viewset school.
    """
    serializer_class = SchoolSerializer
    queryset = School.objects.all()
    lookup_field = "id"
    filter_backends = (DjangoFilterBackend, OrderingFilter, filters.SearchFilter )
    filterset_fields = ["name","max_students"]
    ordering_fields = ["id"]
    search_fields= ['name']



   
