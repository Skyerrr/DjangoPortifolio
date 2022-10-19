from typing import Type
from rest_framework.request import Request
from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.cache import cache
from django.contrib.auth import authenticate, login, logout
from django.template.defaulttags import register
from django.http import Http404

# import redis
from .. import models, forms

# Create your views here.


def clear_all_cache():
    # the_redis = redis.Redis()
    # the_redis.flushall()
    cache.clear()


def index_view(request: Type[Request]) -> Type[HttpResponse]:

    all_category = models.Category.objects.all()

    context = {"all_category": all_category}
    return render(request, "br/index.html", context)


def about_view(request: Type[Request]) -> Type[HttpResponse]:

    all_category = models.Category.objects.all()

    context = {"all_category": all_category}
    return render(request, "br/about.html", context)


def faq_view(request: Type[Request]) -> Type[HttpResponse]:

    all_category = models.Category.objects.all()

    context = {"all_category": all_category}
    return render(request, "br/faq.html", context)


def subcategory_detail_view(request: Type[Request], br_name: str) -> Type[HttpResponse]:

    if cache.get(br_name) and cache.get(f"{br_name}vehicles"):

        print("DATA FROM CACHE")
        subcategory = cache.get(br_name)
        all_vehicles = cache.get(f"{br_name}vehicles")

    else:
        try:
            subcategory = models.SubCategory.objects.get(br_name=br_name)
            all_vehicles = models.Vehicles.objects.filter(subcategory_id=subcategory.id)
            cache.set(br_name, subcategory)
            cache.set(f"{br_name}vehicles", all_vehicles)
            print("DATA FROM DB")

        except models.SubCategory.DoesNotExist as exc:
            raise Http404("News does not exist") from exc
    all_category = models.Category.objects.all()
    context = {
        "subcategory": subcategory,
        "all_vehicles": all_vehicles,
        "all_category": all_category,
    }

    return render(request, "br/categoria.html", context)


def vehicle_detail_view(
    request: Type[Request], br_name: str, br_title: str
) -> Type[HttpResponse]:

    if (
        cache.get(br_name)
        and cache.get(f"{br_name}{br_title}vehicle")
        and cache.get(f"{br_name}{br_title}gallery")
    ):

        print("DATA FROM CACHE")
        subcategory = cache.get(br_name)
        vehicle = cache.get(f"{br_name}{br_title}vehicle")
        all_gallery = cache.get(f"{br_name}{br_title}gallery")
        print(all_gallery)

    else:
        try:
            subcategory = models.SubCategory.objects.get(br_name=br_name)
            vehicle = models.Vehicles.objects.get(br_title=br_title)
            all_gallery = models.Gallery.objects.filter(vehicle_id=vehicle.id)
            cache.set(br_name, subcategory)
            cache.set(f"{br_name}{br_title}vehicle", vehicle)
            cache.set(f"{br_name}{br_title}gallery", all_gallery)
            print("DATA FROM DB")

        except models.Vehicles.DoesNotExist as exc:
            raise Http404("News does not exist") from exc

    all_category = models.Category.objects.all()

    context = {
        "subcategory": subcategory,
        "vehicle": vehicle,
        "all_category": all_category,
        "all_gallery": all_gallery,
    }
    return render(request, "br/vehicle.html", context)


def vehicle_add_view(request: Type[Request]):
    all_category = models.Category.objects.all()
    form = forms.VehiclesForm()
    context = {"form": form, "all_category": all_category}

    if request.method == "POST":
        form = forms.VehiclesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = forms.VehiclesForm(request.POST, request.FILES)
            clear_all_cache()
            return redirect("br_index")

        else:
            form = forms.VehiclesForm(request.POST)
            return render(request, "br/edit.html", context)

    return render(request, "br/edit.html", context)


def vehicle_edit_view(request: Type[Request], br_title: str):
    all_category = models.Category.objects.all()
    vehicle = get_object_or_404(models.Vehicles, br_title=br_title)
    form = forms.VehiclesForm(instance=vehicle)
    context = {"form": form, "vehicle": vehicle, "all_category": all_category}

    if request.method == "POST":
        form = forms.VehiclesForm(request.POST, request.FILES, instance=vehicle)
        if form.is_valid():
            form.save()
            form = forms.VehiclesForm(request.POST, request.FILES, instance=vehicle)
            clear_all_cache()
            return redirect(
                "br_vehicle", vehicle.subcategory_id.br_name, vehicle.br_title
            )

        else:
            form = forms.VehiclesForm(request.POST, instance=vehicle)
            return render(request, "br/edit.html", context)

    return render(request, "br/edit.html", context)


def gallery_edit_view(request: Type[Request], vehicle_id: int):
    all_category = models.Category.objects.all()
    all_gallery = models.Gallery.objects.filter(vehicle_id=vehicle_id)

    form = forms.GalleryForm(initial={"vehicle_id": vehicle_id})
    context = {"form": form, "all_gallery": all_gallery, "all_category": all_category}

    if request.method == "POST":
        form = forms.GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = forms.GalleryForm(request.POST, request.FILES)
            clear_all_cache()
            return redirect("edit_gallery", vehicle_id)

        else:
            form = forms.GalleryForm(request.POST, request.FILES)
            return redirect("edit_gallery", vehicle_id)

    return render(request, "br/editgallery.html", context)


def delete_vehicle(request: Type[Request], id: int):
    vehicle = get_object_or_404(models.Vehicles, id=id)
    vehicle.delete()
    clear_all_cache()
    return redirect(
        "br_index",
    )


def delete_gallery(request: Type[Request], id: int, vehicle_id: int):
    gallery = get_object_or_404(models.Gallery, id=id)
    gallery.delete()
    clear_all_cache()
    return redirect("edit_gallery", vehicle_id)


def billylogin(request: Type[Request]):
    if request.method == "GET":
        context = ""
        return render(request, "br/login.html", {"context": context})

    elif request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/billymods/pt-br")
        else:
            context = {"error": "Wrong credintials"}
            return render(request, "br/login.html", {"context": context})


def billylogout(request):
    logout(request)
    return HttpResponseRedirect("/billymods/pt-br")


@register.filter
def percentage_br(obj):
    new_price = float(obj.discount_value / 100 * obj.br_price - obj.br_price) * (-1)
    return new_price
