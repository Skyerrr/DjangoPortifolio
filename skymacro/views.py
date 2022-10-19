from typing import Type
from rest_framework.request import Request
from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import FileResponse
from django.conf import settings

# Create your views here.


def skymacro_view(request: Type[Request]) -> Type[HttpResponse]:
    """
    View function to render about page
    return about.html
    """

    return render(request, "skymacro.html")


def download_skymacro(request: Type[Request]) -> Type[FileResponse]:
    """
    View function to download skymacro file
    """
    print(settings.BASE_DIR)
    skymacro = open(
        f"{settings.BASE_DIR}/skymacro/outputs/SkyMacroSetup.exe",
        "rb",
    )
    response = FileResponse(skymacro)

    return response
