from rest_framework import serializers
from .models import Students
from ac_users.models import CustomUser



class CourseStudentsSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source="custom_user.name", read_only=True)
    course_name = serializers.CharField(source="course.name", read_only=True)

    class Meta:
        model = Students
        fields = ['custom_user', 'course', 'student_name', 'course_name']

