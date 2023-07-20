from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from .models import Noticia
from .forms import NoticiaForm
     
def listar_noticias(request):
    noticias = Noticia.objects.order_by('-fecha_publicacion')
    return render(request, 'listar_noticias.html', {'noticias': noticias})

def crear_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_noticias')
    else:
        form = NoticiaForm()
    return render(request, 'crear_noticia.html', {'form': form})

def editar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    if request.method == 'POST':
        form = NoticiaForm(request.POST, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('listar_noticias')
    else:
        form = NoticiaForm(instance=noticia)
    return render(request, 'editar_noticia.html', {'form': form, 'noticia': noticia})

def eliminar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    if request.method == 'POST':
        noticia.delete()
        return redirect('listar_noticias')
    return render(request, 'eliminar_noticia.html', {'noticia': noticia})

def acerca_de(request):
    return render(request, 'acerca_de.html')

def contacto(request):
    return render(request, 'contacto.html')
