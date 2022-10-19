from typing import Type
from rest_framework.request import Request
from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.cache import cache_page

# Create your views here.


def index_view(request: Type[Request]) -> Type[HttpResponse]:
    """
    View function to render about page
    return about.html
    """
    return render(request, "home.html")
