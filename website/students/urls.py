from django.urls import path
from .views import *

urlpatterns = [
    path('students/', AllStudentsAPIList.as_view()),
    path("course_students/", AllCourseStudentsListView.as_view()),
    path("course_students/<int:pk>/", CourseStudentsDetailView.as_view()),
    path("students/<int:pk>/courses/", StudentsCourseList.as_view()),
    path("students/<int:pk>/homeworks/", StudentsHomeworkListView.as_view()),
    path("students/<int:pk_student>/lectures/<int:pk_lecture>/homeworks/", StudentsLectureHomeworksListCreateView.as_view()),
    path("students/<int:pk>/", StudentsDetailView.as_view())

]