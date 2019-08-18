from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils import timezone

# Create your models here.

User = settings.AUTH_USER_MODEL

class ApplicantQuerySet(models.QuerySet):
    def registered(self):
        return self
        # now = timezone.now()
        # return self.filter(registered_date__lte=now)

    def search(self, query):
        lookup = (
            Q(mykid_no__icontains=query),
            Q(name__icontains=query)
        )

        return self.filter(lookup)


class ApplicantManager(models.Manager):
    def get_queryset(self):
        return ApplicantQuerySet(self.model, using=self._db)

    def registered(self):
        return self.get_queryset().registered()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().registered().search(query)


class Applicant(models.Model):  # Applicant_set -> queryset
    # id = models.IntegerField() # pk
    # creator    = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    mykid_no = models.CharField(max_length=20, null=False, blank=False)
    name = models.CharField(max_length=120)
    address1 = models.CharField(max_length=120)
    address2 = models.CharField(max_length=120)
    address3 = models.CharField(max_length=120)
    registered_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    objects = ApplicantManager()

    class Meta:
        ordering = ['-registered_date', '-modified_date']

    def get_absolute_url(self):
        return f"/registration/applicants/{self.mykid_no}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"
