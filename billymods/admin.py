from django.contrib import admin
from .models import Category, SubCategory, Gallery, Vehicles

# Register your models here.

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Gallery)
admin.site.register(Vehicles)
admin.register(Vehicles)
