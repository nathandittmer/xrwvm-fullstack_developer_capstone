from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.
admin.site.register(CarModel)

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
admin.site.register(CarMake)
