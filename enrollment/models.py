from django.conf import settings
from django.db import models
from django.db.models import Q

# Create your models here.
User = settings.AUTH_USER_MODEL

"""Session"""


class SessionQuerySet(models.QuerySet):
    def opened(self):
        return self.filter(opened=True)

    def closed(self):
        return self.filter(opened=False)

    def search(self, query):
        lookup = (
            Q(code__icontains=query),
            Q(name__icontains=query)
        )
        return self.filter(lookup)


class SessionManager(models.Manager):
    def get_queryset(self):
        return SessionQuerySet(self.model, using=self._db)

    def opened(self):
        return self.get_queryset().opened()

    def closed(self):
        return self.get_queryset().closed()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().closed().search(query)


class Session(models.Model):  # Session_set -> queryset
    # id = models.IntegerField() # pk
    code = models.CharField(max_length=20, null=False, blank=False)
    name = models.CharField(max_length=120)
    opened = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    objects = SessionManager()

    class Meta:
        ordering = ['-code', '-name']

    def get_absolute_url(self):
        return f"/enrollment/sessions/{self.code}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"


"""Student"""


class StudentQuerySet(models.QuerySet):

    def search(self, query):
        lookup = (
            Q(code__icontains=query),
            Q(name__icontains=query)
        )
        return self.filter(lookup)


class StudentManager(models.Manager):
    def get_queryset(self):
        return StudentQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)


class Student(models.Model):  # Student_set -> queryset
    # id = models.IntegerField() # pk
    code = models.CharField(max_length=20, null=False, blank=False)
    name = models.CharField(max_length=120)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    objects = StudentManager()

    class Meta:
        ordering = ['-code', '-name']

    def get_absolute_url(self):
        return f"/enrollment/students/{self.code}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"


class EnrollmentQuerySet(models.QuerySet):

    def search(self, query):
        lookup = (
        )
        return self.filter(lookup)


class EnrollmentManager(models.Manager):
    def get_queryset(self):
        return EnrollmentQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)


class Enrollment(models.Model):
    # id = models.IntegerField() # pk
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    objects = EnrollmentManager()

    class Meta:
        ordering = []

    def get_absolute_url(self):
        return f"/enrollment/enrollments/{self.id}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"
