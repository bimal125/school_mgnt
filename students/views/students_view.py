from students.serializers.StudentSerializer import StudentSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from students.models import Student

class StudentViewSet(viewsets.ModelViewSet):
    """
    A viewset for students.
    """
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = 'id'

