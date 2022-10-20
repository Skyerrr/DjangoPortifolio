from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path("amazonscrap", views.scrap_view, name="scrap_index"),
    path("amazonscrap/download-csv", views.download_amazon_csv, name="csv_download"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
