from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from ac_users.models import User


@receiver(post_save, sender=User)
def create_teacher_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_teacher:
            User.objects.create(user='teacher',
                                   first_name=instance.first_name,
                                   last_name=instance.last_name,
                                   email=instance.email)


@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_student:
            User.objects.create(user='student',
                                   first_name=instance.first_name,
                                   last_name=instance.last_name,
                                   email=instance.email)


# @receiver(post_save, sender=User)
# def create_persona(sender, instance, created, **kwargs):
#     if created:
#         User.objects.create(user=instance)