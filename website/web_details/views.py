from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework import generics, viewsets
from ac_users import serializers as ac_serializers
from rest_framework.permissions import IsAuthenticated
from web_details import serializers as web_serializers
from web_details.models import *
from .serializers import *
from ac_users.models import User
from .models import Lecture
from ac_users.permissions import IsTeacher, ReadOnly


class CustomUserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = ac_serializers.CustomUserSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(custom_user=user)


class CustomUserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ac_serializers.CustomUserSerializer


class TeachersAPIList(generics.ListAPIView):
    serializer_class = CourseTeachersSerializer
    lookup_field = "id"

    def get_queryset(self):
        return User.objects.filter(role='teacher')


class AllTeachersAPIList(generics.ListAPIView):
    queryset = User.objects.filter(role='teacher')
    serializer_class = ac_serializers.CustomUserSerializer


class TeachersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(role='teacher')
    serializer_class = ac_serializers.CustomUserSerializer


class AllStudentsAPIList(generics.ListAPIView):
    queryset = User.objects.filter(role='student')
    serializer_class = ac_serializers.CustomUserSerializer


class StudentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(role='student')
    serializer_class = ac_serializers.CustomUserSerializer


class AllCoursesViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [(IsAuthenticated & ReadOnly) | IsTeacher]


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAuthenticated,)


class AllCourseStudentsListView(generics.ListCreateAPIView):
    queryset = CourseStudents.objects.all()
    serializer_class = CourseStudentsSerializer
    permission_classes = [(IsAuthenticated & ReadOnly) | IsTeacher]


class CourseStudentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseStudents.objects.all()
    serializer_class = CourseStudentsSerializer
    permission_classes = (IsAuthenticated,)


class StudentsCourseList(generics.ListAPIView):
    serializer_class = ac_serializers.CustomUserSerializer
    model = CourseStudents
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        pk = self.kwargs['pk']
        return CourseStudents.objects.filter(user_id=pk).filter(user__role='student')


class CourseLecturesView(generics.ListAPIView):
    serializer_class = LectureSerializer
    model = Lecture
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Lecture.objects.filter(course_id=pk)


class AllCourseTeachersListView(generics.ListCreateAPIView):
    queryset = CourseTeachers.objects.all()
    serializer_class = CourseTeachersSerializer
    queryset = queryset.filter(user__role='teacher')
    permission_classes = (IsAuthenticated,)


class CourseTeachersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseTeachers.objects.all()
    serializer_class = CourseTeachersSerializer
    queryset = queryset.filter(user__role='teacher')
    permission_classes = (IsAuthenticated,)


class TeachersCourseList(generics.ListAPIView):
    serializer_class = ac_serializers.CustomUserSerializer
    model = CourseTeachers
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        pk = self.kwargs['pk']
        return CourseTeachers.objects.filter(user_id=pk).filter(user_role='teacher')


class LecturesListCreateView(generics.ListCreateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = (IsAuthenticated,)


class LecturesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = (IsAuthenticated,)


class HomeworkListView(generics.ListAPIView):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    permission_classes = (IsAuthenticated,)


class HomeworkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    permission_classes = (IsAuthenticated,)


class MarkListCreateView(generics.ListCreateAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
    permission_classes = (IsAuthenticated,)


class MarkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
    permission_classes = (IsAuthenticated,)


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)


class StudentsHomeworkListView(generics.ListAPIView):
    serializer_class = web_serializers.HomeworkSerializer
    model = Homework
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Homework.objects.filter(students_user_id=pk).filter(students_user__role='student')


class StudentsLectureHomeworksListCreateView(generics.ListCreateAPIView):
    serializer_class = web_serializers.HomeworkSerializer
    model = Homework
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        pk_students = self.kwargs['pk_students']
        pk_lecture = self.kwargs['pk_lecture']

        return Homework.objects \
            .filter(students_user_id=pk_students) \
            .filter(lecture_id=pk_lecture) \
            .filter(students_user__role='student')