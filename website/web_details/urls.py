from django.urls import path
from .views import *

urlpatterns = [
    path("courses/", AllCoursesListCreateView.as_view()),
    path("courses/<int:pk>/", CourseDetailView.as_view()),
    path("courses/<int:pk>/lectures/", CourseLecturesView.as_view()),
    path("lectures/", LecturesListCreateView.as_view()),
    path("lectures/<int:pk>/", LecturesDetailView.as_view()),
    path("lectures/<int:pk>/homeworks/", HomeworkListView.as_view()),
    path("marks/<int:pk>/", MarkDetailView.as_view()),
    path("marks/", MarkListCreateView.as_view()),
    path("comments/<int:pk>/", CommentDetailView.as_view()),
    path("comments/", CommentListCreateView.as_view()),
]
