from rest_framework import generics
from ac_users.models import CustomUser
from ac_users import serializers as ac_serializers
from .models import Teachers
from .serializers import CourseTeachersSerializer


class TeachersAPIList(generics.ListAPIView):
    queryset = CustomUser.objects.filter(status='teacher')
    serializer_class = ac_serializers.UserSerializer


class TeachersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.filter(status='teacher')
    serializer_class = ac_serializers.UserSerializer



class AllCourseTeachersListView(generics.ListCreateAPIView):
    queryset = Teachers.objects.all()
    serializer_class = CourseTeachersSerializer
    queryset = queryset.filter(custom_user__status='teacher')



class CourseTeachersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teachers.objects.all()
    serializer_class = CourseTeachersSerializer
    queryset = queryset.filter(custom_user__status='teacher')


class TeachersCourseList(generics.ListAPIView):
    serializer_class = ac_serializers.UserSerializer
    model = Teachers

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Teachers.objects.filter(custom_user_id=pk).filter(cusom_user__status='teacher')


