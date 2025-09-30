from django.shortcuts import render, get_object_or_404
from .forms import ContactoForm
from .models import PreguntaFrecuente, Videojuego, Contacto

def index(request):
    mensaje_exito = None  

    if request.method == 'POST':
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        asunto = request.POST.get("asunto")
        mensaje = request.POST.get("mensaje")
        
        # Guardar en la base de datos
        contacto = Contacto(
            nombre=nombre,
            email=email,
            asunto=asunto,
            mensaje=mensaje
        )
        contacto.save()

        mensaje_exito = "¡Tu mensaje ha sido enviado con éxito!"
        
    return render(request, 'index.html', {
        'mensaje_exito': mensaje_exito
    })

def fyq(request):
    preguntas = PreguntaFrecuente.objects.all()
    return render(request, 'fyq.html', {'preguntas': preguntas})

def open_view(request):
    videojuegos = Videojuego.objects.all()
    return render(request, 'open.html', {'videojuegos': videojuegos})


