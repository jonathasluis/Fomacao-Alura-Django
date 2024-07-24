from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


from galeria.models import Fotografia

@login_required
def index(request):

    fotografias = Fotografia.objects.order_by("-data_fotofrafia").filter(publicado=True)
    return render(request, 'galeria/index.html', {"cards" : fotografias})

@login_required
def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

@login_required
def buscar(request):
    fotografias = Fotografia.objects.order_by("data_fotofrafia").filter(publicado=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar: 
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render (request, "galeria/buscar.html", {"cards": fotografias})
