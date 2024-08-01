from django.urls import path
from . views import *

urlpatterns = [
    path("av/", addview),
    path("sv/", showview),
    path("uv/<int:id>", updateview),
    path("dv/<int:pk>", deleteview)
]