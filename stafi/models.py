from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission

class Profesori(models.Model):

    emri = models.CharField(max_length=255)
    mbiemri=models.CharField(max_length=255)
    cel=models.CharField(max_length=10)
    email = models.CharField(max_length=255)


def __str__(self):
    return f"Profesori: {self.emri} {self.mbiemri}"

class Subject(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


@staticmethod
def get_or_create_default_subject():
    default_subject_name = ""
    default_subject, _ = Subject.objects.get_or_create(name=default_subject_name)
    return default_subject.pk

class Kurset(models.Model):
    leksioni = models.FileField(max_length=2080)
    petagogu=models.CharField(max_length=255)
    kredite= models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return f"{self.leksioni} - {self.subject}"



class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, is_student=False, **extra_fields):
        if not email:
            raise ValueError("Duhet te vendosni emailin")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_student=is_student, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)
class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(Group, blank=True, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_users')
    objects = CustomUserManager()
