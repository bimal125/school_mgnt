from rest_framework import serializers
from students.models import Student

class StudentSerializer(serializers.ModelSerializer):
    roll_no = serializers.CharField(read_only=True)
    id = serializers.CharField(read_only=True)

    def validate_age(self,value):
        if 4 <= value <= 70:
            return value
        else:
            raise serializers.ValidationError('Age should be between 4 to 70.')

    def validate_school(self,value):
        max_students_limit = value.max_students
        total_students = value.student_set.all().count()
        if total_students >= max_students_limit:
            raise serializers.ValidationError('Maximum student limit reached.')
        else:
            return value

    class Meta:
        model = Student
        fields = ('fname','lname','roll_no','school','id','nationality','sex','age')
        lookup_field = 'id'
        extra_kwargs = {
            'url': {'lookup_field': 'id'}
        }

    
