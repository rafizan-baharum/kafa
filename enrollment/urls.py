from django.urls import path
from .views import (
    session_detail_view,
    session_list_view,
    session_update_view,
    session_delete_view,
    session_create_view)

urlpatterns = [
    path('sessions/', session_list_view),
    path('sessions/<str:code>/', session_detail_view),
    path('sessions/create', session_create_view),
    path('sessions/<str:code>/edit/', session_update_view),
    path('sessions/<str:code>/delete/', session_delete_view),
]
