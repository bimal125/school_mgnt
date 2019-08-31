from rest_framework import serializers
from schools.models import School

class SchoolSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    class Meta:
        model = School
        fields = ('name','max_students','id')
        lookup_field = 'id'
        extra_kwargs = {
            'url': {'lookup_field': 'id'}
        }
