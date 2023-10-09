from django.shortcuts import render, redirect
from .models import Mensaje
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def lista_mensajes(request):
    mensajes = Mensaje.objects.filter(receptor=request.user).order_by('-fecha_envio')
    return render(request, 'lista_mensajes.html', {'mensajes': mensajes})

@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        contenido = request.POST['contenido']
        receptor_id = request.POST['receptor_id']
        receptor = User.objects.get(id=receptor_id)
        mensaje = Mensaje(emisor=request.user, receptor=receptor, contenido=contenido)
        mensaje.save()
        messages.success(request, 'Mensaje enviado con éxito.')
        return redirect('lista_mensajes')
    return redirect('lista_mensajes')


@login_required
def lista_mensajes(request):
    mensajes = Mensaje.objects.filter(receptor=request.user).order_by('-fecha_envio')
    usuarios = User.objects.exclude(id=request.user.id)  # Excluye al usuario actual
    return render(request, 'messages/lista_mensajes.html', {'mensajes': mensajes, 'usuarios': usuarios})
