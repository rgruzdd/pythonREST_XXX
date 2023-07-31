from django.urls import path, include
from rest_framework import routers

from . import views
from .views import *

router = routers.SimpleRouter()
router.register(r'courses', AllCoursesViewSet)


urlpatterns = [
    path("courses/", include(router.urls)),
    path("courses/<int:pk>/", views.CourseDetailView.as_view()),
    path("courses/<int:pk>/lectures/", views.CourseLecturesView.as_view()),
    path("lectures/", views.LecturesListCreateView.as_view()),
    path("lectures/<int:pk>/", views.LecturesDetailView.as_view()),
    path("lectures/<int:pk>/homeworks/", views.HomeworkListView.as_view()),
    path("marks/<int:pk>/", views.MarkDetailView.as_view()),
    path("marks/", views.MarkListCreateView.as_view()),
    path("comments/<int:pk>/", views.CommentDetailView.as_view()),
    path("comments/", views.CommentListCreateView.as_view()),
    path('teachers/', views.AllTeachersAPIList.as_view()),
    path("course_teachers/", views.AllCourseTeachersListView.as_view()),
    path("course_teacher/<int:pk>/", views.CourseTeachersDetailView.as_view()),
    path("teachers/<int:pk>/courses/", views.HomeworkDetailView.as_view()),
    path("teachers/<int:pk>/", views.TeachersDetailView.as_view()),
    path('students/', views.AllStudentsAPIList.as_view()),
    path("course_students/", views.AllCourseStudentsListView.as_view()),
    path("course_students/<int:pk>/", views.CourseStudentsDetailView.as_view()),
    path("students/<int:pk>/courses/", views.StudentsCourseList.as_view()),
    path("students/<int:pk>/homeworks/", views.StudentsHomeworkListView.as_view()),
    path("students/<int:pk_student>/lectures/<int:pk_lecture>/homeworks/",
         views.StudentsLectureHomeworksListCreateView.as_view()),
    path("students/<int:pk>/", views.StudentsDetailView.as_view())
]
