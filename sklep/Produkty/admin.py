from django.contrib import admin
from .models import Producent, Produkty, Kategoria
                                                        # Register your models here.
admin.site.register(Produkty)
admin.site.register(Producent)
admin.site.register(Kategoria)