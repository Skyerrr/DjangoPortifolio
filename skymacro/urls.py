from django.urls import path
from . import views

urlpatterns = [
    path("skymacro", views.skymacro_view, name="skymacro"),
    path("skymacro/download", views.download_skymacro, name="skymacro_download"),
]
