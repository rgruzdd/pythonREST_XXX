from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework import generics
from ac_users import serializers as ac_serializers
from web_details.models import *
from .serializers import *
from ac_users.models import CustomUser

from web_details.models import Course

from .models import Lecture


class CustomUserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ac_serializers.UserSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class CustomUserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ac_serializers.UserSerializer


class AllCoursesListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LecturesListCreateView(generics.ListCreateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer


class LecturesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer


class CourseLecturesView(generics.ListAPIView):
    serializer_class = LectureSerializer
    model = Lecture

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Lecture.objects.filter(course_id=pk)


class HomeworkListView(generics.ListAPIView):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer


class HomeworkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer


class MarkListCreateView(generics.ListCreateAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer


class MarkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
