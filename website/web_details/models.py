from django.db import models

from ac_users.models import CustomUser


class Course(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Lecture(models.Model):
    title = models.CharField(max_length=200)
    present_file_name = models.CharField(max_length=200)
    hometask = models.TextField(blank=False)
    course = models.ForeignKey(Course, related_name='course_lectures', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Homework(models.Model):
    solution_link = models.CharField(max_length=500)
    student_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, related_name="homeworks", on_delete=models.CASCADE)

    def __str__(self):
        return f"Homework Student: {self.student_user.name}, Solution: {self.solution_link}, Lecture: {self.lecture.title}"


class Mark(models.Model):
    homework = models.OneToOneField(Homework, related_name='rel_mark', on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self):
        return f'{self.value}'


class Comment(models.Model):
    body = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    mark = models.ForeignKey(Mark, related_name='comments', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'User: {self.user.name} Text: {self.body}'
