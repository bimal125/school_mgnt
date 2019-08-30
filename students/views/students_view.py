from students.serializers.StudentSerializer import StudentSerializer
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from students.models import Student
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework import generics

class StudentViewSet(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   GenericViewSet):
    """
    Student viewset
    """
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = 'id'


    

class ListStudent(generics.ListAPIView):
    """
    get students
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, )
    filterset_fields = ("fname","lname","roll")
    ordering_fields = ("id","roll",)
    ordering = ("roll")
    search_fields= ("fname","lname","roll")

