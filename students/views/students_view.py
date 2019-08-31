from students.serializers.StudentSerializer import StudentSerializer
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from students.models import Student
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import filters

class StudentViewSet(viewsets.ModelViewSet):
    """
    Student viewset
    """
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = "id"
    filter_backends = (DjangoFilterBackend, OrderingFilter, filters.SearchFilter )
    filterset_fields = ["nationality","sex","age"]
    ordering_fields = ["id"]
    search_fields= ['nationality','fname','lname']





