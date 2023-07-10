from django.shortcuts import render, HttpResponse
from .models import Noticia
# Create your views here.


# def inicio(request):
#     return HttpResponse("<h1>HOLA MUNDO</h1> <h2> desde django</h2>")

# decorador para ver las noticias solamente como usuario logueado
from django.contrib.auth.decorators import login_required

# uso de decorador para verificar logeo de usuario y poder ver noticia


@login_required
def inicio(request):

    ctx = {}
    # clase.objetcs.all()==> select * from noticia
    noticia = Noticia.objects.all()
    ctx["noticias"] = noticia
    return render(request, 'noticias/inicio.html', ctx)

# ClaseName.objects.all()              select * from noticias
# ClaseName.objects.get(pk = 1)        select * from noticias where id = 1
# ClaseName.objects.filter(categoria)  select * from noticias where categoria = deportes
