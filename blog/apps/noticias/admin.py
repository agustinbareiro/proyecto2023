from django.contrib import admin

from .models import Categoria, Noticia, Contacto
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Noticia)
admin.site.register(Contacto)
