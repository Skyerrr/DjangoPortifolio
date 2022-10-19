from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
import redis

# Create your models here.


class Category(models.Model):
    en_name = models.CharField(max_length=255, unique=True)
    br_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.id}- {self.en_name} | {self.br_name}"


class SubCategory(models.Model):
    en_name = models.CharField(max_length=255, unique=True)
    br_name = models.CharField(max_length=255, unique=True)
    category_id = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="subcategories"
    )

    def __str__(self):
        return f"{self.id}- {self.en_name} | {self.br_name}"


class Vehicles(models.Model):

    en_title = models.CharField(max_length=255, unique=True)
    br_title = models.CharField(max_length=255, unique=True)
    en_description = models.CharField(max_length=255, null=True)
    br_description = models.CharField(max_length=255, null=True)
    en_body = RichTextField()
    br_body = RichTextField()
    image = models.ImageField(upload_to="billymods", null=True, blank=True)
    video = models.CharField(max_length=255, blank=True)
    image_video = models.ImageField(upload_to="billymods", null=True, blank=True)
    br_price = models.FloatField(null=False)
    en_price = models.FloatField(null=False)
    discount_value = models.FloatField(null=False, blank=False)
    tebex = models.CharField(max_length=255, null=True)

    subcategory_id = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, related_name="vehicles"
    )

    def __str__(self):
        return f"{self.id}- {self.en_title} | {self.br_title}"


class Gallery(models.Model):
    images = models.ImageField(upload_to="billymods")
    vehicle_id = models.ForeignKey(
        Vehicles, on_delete=models.CASCADE, related_name="gallery"
    )

    def __str__(self):
        return f"{self.images}"
