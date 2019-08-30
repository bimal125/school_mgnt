from schools.serializers.SchoolSerializer import SchoolSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from schools.models import School

class SchoolViewSet(viewsets.ModelViewSet):
    """
    A viewset for schools.
    """
    serializer_class = SchoolSerializer
    queryset = School.objects.all()
    lookup_field = 'id'

