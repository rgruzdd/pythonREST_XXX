from django.db import models
from ac_users.models import CustomUser
from web_details.models import Course


class Students(models.Model):
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="student_courses")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_students")

    def __str__(self):
        return self


