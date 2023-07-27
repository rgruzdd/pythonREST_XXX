from django.contrib.auth.models import User, AbstractUser
from django.db import models


class User(AbstractUser):
    STATUS_CHOICES = (
        ('teacher', 'teacher'),
        ('student', 'student'),
        ('staff', 'staff')
    )
    USERNAME_FIELD = 'email'
    first_name = models.CharField(('first_name'), max_length=150)
    last_name = models.CharField(('last name'), max_length=150)
    email = models.EmailField(('email address'), unique=True)
    role = models.CharField(verbose_name='role', max_length=30, choices=STATUS_CHOICES)
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    @property
    def is_teacher(self):
        if self.role == 'teacher':
            return True
        else:
            return False





    # is_staff = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)
    # title = models.CharField(max_length=255)
    # content = models.TextField(blank=True)
    # time_create = models.DateTimeField(auto_now_add=True)
    # time_update = models.DateTimeField(auto_now=True)
    # is_published = models.BooleanField(default=True)
    # cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    # user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    #     first_name = models.CharField(('first_name'), max_length=150)
    #     last_name = models.CharField(('last name'), max_length=150)
    #     email = models.EmailField(('email address'), unique=True)
    #     role = models.CharField(verbose_name='role', max_length=30, choices=STATUS_CHOICES)
    #     is_staff = models.BooleanField(default=False)
    #     is_superuser = models.BooleanField(default=False)
    #     is_active = models.BooleanField(default=True)
    #     token = models.CharField(max_length=250)



# class UserManager(BaseUserManager):
#     def _generate_jwt_token(self):
#         dt = datetime.now() + timedelta(days=30)
#
#         token = jwt.encode({
#             'id': self.pk,
#             'exp': dt
#         }, settings.SECRET_KEY, algorithm='HS256')
#
#         return token
#
#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)
#
#         if not extra_fields.get('is_staff'):
#             raise ValueError("Superuser must have is_staff = True")
#
#         if not extra_fields.get('is_superuser'):
#             raise ValueError("Superuser must have is_superuser = True")
#         return self.create_user(email, password, **extra_fields)


1
# class CustomUser(AbstractUser):
#     STATUS_CHOICES = (
#         ('teacher', 'teacher'),
#         ('student', 'student'),
#         ('staff', 'staff')
#     )
#
#     first_name = models.CharField(('first_name'), max_length=150)
#     last_name = models.CharField(('last name'), max_length=150)
#     email = models.EmailField(('email address'), unique=True)
#     role = models.CharField(verbose_name='role', max_length=30, choices=STATUS_CHOICES)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     token = models.CharField(max_length=250)
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = [ 'email', 'password']
#
#     def __str__(self):
#         return '{} : {}'.format(self.username, self.get_role_display())
#
#     def __str__(self):
#         return self.email
#
#     @property
#     def token(self):
#         """
#         Позволяет получить токен пользователя путем вызова user.token, вместо
#         user._generate_jwt_token(). Декоратор @property выше делает это
#         возможным. token называется "динамическим свойством".
#         """
#         return self._generate_jwt_token()

    # def has_module_perms(self, app_label):
    #     return True
    #
    # def has_perm(self, perm, obj=None):
    #     return True
    #
    # objects = UserManager()
1



