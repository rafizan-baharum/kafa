from django.urls import path
from .views import (
    applicant_detail_view,
    applicant_list_view,
    applicant_update_view,
    applicant_delete_view,
    applicant_create_view)

urlpatterns = [
    path('applicants/', applicant_list_view),
    path('applicants/<str:mykid_no>/', applicant_detail_view),
    path('applicants/create', applicant_create_view),
    path('applicants/<str:mykid_no>/edit/', applicant_update_view),
    path('applicants/<str:mykid_no>/delete/', applicant_delete_view),
]
