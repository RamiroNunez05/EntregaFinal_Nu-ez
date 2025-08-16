from django.contrib import admin
from .models import Familiar, Vuelo, Compra

# Register your models here.
register_models = [Familiar, Vuelo, Compra]

admin.site.register(register_models)