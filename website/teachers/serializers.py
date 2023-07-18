from rest_framework import serializers
from .models import Teachers
from ac_users.models import CustomUser




class CourseTeachersSerializer(serializers.ModelSerializer):
    teacher_name = serializers.CharField(source="custom_user.name", read_only=True)
    course_name = serializers.CharField(source="course.name", read_only=True)

    class Meta:
        model = Teachers
        fields = ['custom_user', 'course', 'teacher_name', 'course_name']

