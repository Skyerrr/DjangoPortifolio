from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path("billymods/en-us", views.index_view, name="en_index"),
    path("billymods/en-us/about", views.about_view, name="en_about"),
    path("billymods/en-us/faq", views.faq_view, name="en_faq"),
    path(
        "billymods/en-us/<str:en_name>",
        views.subcategory_detail_view,
        name="en_subcategory",
    ),
    path("billymods/en-us/login/", views.billylogin, name="en_billylogin"),
    path("billymods/logout", views.billylogout, name="en_billylogout"),
    path(
        "billymods/delete_vehicle/<int:id>",
        login_required(views.delete_vehicle),
        name="delete_vehicle",
    ),
    path(
        "billymods/delete_gallery/<int:id>/<int:vehicle_id>",
        login_required(views.delete_gallery),
        name="delete_gallery",
    ),
    path(
        "billymods/en-us/edit/<str:en_title>",
        login_required(views.vehicle_edit_view),
        name="en_edit_vehicle",
    ),
    path(
        "billymods/en-us/editgallery/<int:vehicle_id>",
        login_required(views.gallery_edit_view),
        name="edit_gallery",
    ),
    path(
        "billymods/en-us/add/vehicle",
        login_required(views.vehicle_add_view),
        name="en_add_vehicle",
    ),
    path(
        "billymods/en-us/<str:en_name>/<str:en_title>",
        views.vehicle_detail_view,
        name="en_vehicle",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
