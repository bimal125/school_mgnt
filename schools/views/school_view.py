from schools.serializers.SchoolSerializer import SchoolSerializer
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from schools.models import School
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework import generics

class SchoolViewSet(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   GenericViewSet):
    """
    School viewset school.
    """
    serializer_class = SchoolSerializer
    queryset = School.objects.all()
    lookup_field = 'id'

class ListSchool(generics.ListAPIView):
    """
    get schools
    """
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, )
    filterset_fields = ("name",)
    ordering_fields = ("max_students",)


   
