from django.urls import path, include

from . import views

app_name = "field"

urlpatterns = [
    path("", views.config, name="config"),
    path("<str:field_name>", views.config, name="config"),
]