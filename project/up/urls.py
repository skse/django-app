from django.urls import path

from up.views import index, databases

urlpatterns = [
    path("", index, name="index"),
    path("databases", databases, name="databases"),
]
