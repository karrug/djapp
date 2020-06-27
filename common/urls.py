from django.urls import path, include
from common.views import index

urlpatterns = [
    path("", index, name="index"),
]
