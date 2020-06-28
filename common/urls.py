from django.urls import path, include
from common.views import index, get_data, set_data

urlpatterns = [
    path("", index, name="index"),
    path("get", get_data, name="get_data"),
    path("set", set_data, name="set_data"),
]
