from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("entry", views.entry, name="name"),
    path("<str:name>", views.entry, name="name"),
    path("create", views.create, name="create"),
]
