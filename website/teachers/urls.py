from django.urls import path
from .views import *
from web_details.views import HomeworkDetailView


urlpatterns = [
    path('teachers/', TeachersAPIList.as_view()),
    path("course_teachers/", AllCourseTeachersListView.as_view()),
    path("course_teacher/<int:pk>/", CourseTeachersDetailView.as_view()),
    path("teachers/<int:pk>/courses/", HomeworkDetailView.as_view()),
    path("teachers/<int:pk>/", TeachersDetailView.as_view())
]