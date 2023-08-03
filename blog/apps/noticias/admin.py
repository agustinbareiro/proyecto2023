from django.contrib import admin

from .models import Categoria, Noticia, Contacto, Comentario
# Register your models here.


class NoticiaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria_noticia", "fecha")
    ordering = ("-fecha",)
    list_filter = ("categoria_noticia",)


admin.site.register(Categoria)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Contacto)
admin.site.register(Comentario)
