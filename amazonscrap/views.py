from typing import Type
from requests import request
from rest_framework.request import Request
from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaulttags import register
from django.http import Http404, FileResponse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.conf import settings
import sys
from . import run

# Create your views here.


def scrap_view(request: Type[Request]) -> Type[HttpResponse]:
    """
    View function to render about page
    return about.html
    """
    if request.method == "GET":

        context = ""
        return render(request, "amazonscrap.html", {"context": context})

    elif request.method == "POST":
        scrapname = request.POST.get("scrapname", "")
        run.run_scrap(scrapname)
        return redirect("scrap_index")


def download_amazon_csv(request: Type[Request]) -> Type[FileResponse]:
    """
    View function to download csv file
    """
    csv = open(
        f"{settings.BASE_DIR}/media/csvfile.csv",
        "rb",
    )
    response = FileResponse(csv)

    return response
