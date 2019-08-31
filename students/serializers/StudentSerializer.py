from rest_framework import serializers
from students.models import Student

class StudentSerializer(serializers.ModelSerializer):
    roll_no = serializers.CharField(read_only=True)
    id = serializers.CharField(read_only=True)
    class Meta:
        model = Student
        fields = ('fname','lname','roll_no','school','id','nationality','sex','age')
        lookup_field = 'id'
        extra_kwargs = {
            'url': {'lookup_field': 'id'}
        }
