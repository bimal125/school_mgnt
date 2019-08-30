from rest_framework import serializers
from students.models import Student

class StudentSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Student
        fields = ('fname','lname','roll','school','id')
        lookup_field = 'id'
        extra_kwargs = {
            'url': {'lookup_field': 'id'}
        }
