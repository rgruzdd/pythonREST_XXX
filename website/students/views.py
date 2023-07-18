from rest_framework import generics
from ac_users.models import CustomUser
from ac_users import serializers as ac_serializers
from web_details import serializers as web_serializers
from .serializers import CourseStudentsSerializer
from .models import Students
from web_details.models import Homework


class AllStudentsAPIList(generics.ListAPIView):
    queryset = CustomUser.objects.filter(status='student')
    serializer_class = ac_serializers.UserSerializer


class StudentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.filter(status='student')
    serializer_class = ac_serializers.UserSerializer


class AllCourseStudentsListView(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = CourseStudentsSerializer


class CourseStudentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = CourseStudentsSerializer


class StudentsCourseList(generics.ListAPIView):
    serializer_class = ac_serializers.UserSerializer
    model = Students

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Students.objects.filter(user_id=pk).filter(user__status='student')


class StudentsHomeworkListView(generics.ListAPIView):
    serializer_class = web_serializers.HomeworkSerializer
    model = Homework

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Homework.objects.filter(students_user_id=pk).filter(students_user__status='student')


class StudentsLectureHomeworksListCreateView(generics.ListCreateAPIView):
    serializer_class = web_serializers.HomeworkSerializer
    model = Homework

    def get_queryset(self):
        pk_students = self.kwargs['pk_students']
        pk_lecture = self.kwargs['pk_lecture']

        return Homework.objects \
            .filter(students_user_id=pk_students) \
            .filter(lecture_id=pk_lecture) \
            .filter(students_user__status='student')

