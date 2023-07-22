from django.shortcuts import render, HttpResponse

# Create your views here.


# def inicio(request):
#     return HttpResponse("<h1>HOLA MUNDO</h1> <h2>desde django</h2>") 

# crear una nueva noticia
from django.shortcuts import render, redirect
from .forms import NoticiaForm
from .models import Noticia

def crear_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_noticias')
    else:
        form = NoticiaForm()
    return render(request, 'crear_noticia.html', {'form': form})

# leer noticia
from django.shortcuts import render
from .models import Noticia

def lista_noticias(request):
    noticias = Noticia.objects.all().order_by('-fecha_publicacion')
    return render(request, 'lista_noticias.html', {'noticias': noticias})

# editar una noticia
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NoticiaForm
from .models import Noticia

def editar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    if request.method == 'POST':
        form = NoticiaForm(request.POST, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('ver_noticia', noticia_id=noticia_id)
    else:
        form = NoticiaForm(instance=noticia)
    return render(request, 'editar_noticia.html', {'form': form, 'noticia': noticia})

# eliminar una noticia
from django.shortcuts import render, get_object_or_404, redirect
from .models import Noticia

def eliminar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    if request.method == 'POST':
        noticia.delete()
        return redirect('lista_noticias')
    return render(request, 'eliminar_noticia.html', {'noticia': noticia})
