from django.urls import path

from coacher.reminders import views

urlpatterns = [
    path("debug", views.debug),
    path("debug/<str:debug_id>", views.debug_by_id)
]
