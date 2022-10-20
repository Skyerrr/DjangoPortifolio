from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path("billymods/pt-br", views.index_view, name="br_index"),
    path("billymods/pt-br/sobre", views.about_view, name="br_about"),
    path("billymods/pt-br/faq", views.faq_view, name="br_faq"),
    path(
        "billymods/pt-br/<str:br_name>",
        views.subcategory_detail_view,
        name="br_subcategory",
    ),
    path("billymods/pt-br/login/", views.billylogin, name="br_billylogin"),
    path("billymods/logout", views.billylogout, name="br_billylogout"),
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
        "billymods/pt-br/edit/<str:br_title>",
        login_required(views.vehicle_edit_view),
        name="edit_vehicle",
    ),
    path(
        "billymods/pt-br/add/vehicle",
        login_required(views.vehicle_add_view),
        name="br_add_vehicle",
    ),
    path(
        "billymods/pt-br/editgallery/<int:vehicle_id>",
        login_required(views.gallery_edit_view),
        name="edit_gallery",
    ),
    path(
        "billymods/pt-br/<str:br_name>/<str:br_title>",
        views.vehicle_detail_view,
        name="br_vehicle",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
