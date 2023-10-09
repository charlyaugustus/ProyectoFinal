from django.http import *
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import *
from django.contrib.auth.models import *
from .models import *
from .forms import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import re
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError




# Create your views here.
def tipo_ser(req, servicio, evento, email):
    servicio = Tipo_Servicio(servicio = servicio, evento = evento, email = email)
    servicio.save()
    
    return HttpResponse(f"""
    
    <p>Tipo de Servicio: {servicio.nombre} - Evento: {servicio.evento}  - Email: {servicio.email} creado con éxito!</p>
    
    """)
@login_required
def listaServicios(req):
    
    servicios = Tipo_Servicio.objects.all()
    return render(req, "ListaServicios.html", {"servicios":servicios})


def inicio(req):
    try:
        avatar = Avatar.objects.get(user=req.user.id)
        return render(req, "inicio.html", {"url_avatar": avatar.imagen.url})
    except:
        return render(req, "inicio.html")
    
def mostrar_eventos(req):
    
    return render(req, "shows.html")

def about(req):
    
    return render(req, "About.html")

def tipo(req):
    return render(req, "servicio.html")

def tipo(req):
    return render(req, "servicio.html")


def clientes(req):
    return render(req, "clientes.html")


def lugar(req):
    return render(req, "lugar.html")


def fecha_entregar(req):
    return render(req, "fecha_entregar.html")

def servicioFormulario(req):
    
    print('method', req.method)
    print('POST',  req.POST)
    
    if req.method == 'POST':
        
        miFormulario = ServicioFormulario(req.POST)
        
        # Validar si el formulario es válido y si el campo email contiene '@'
        if miFormulario.is_valid():
            if re.search(r'@', miFormulario.cleaned_data["email"]):
                data = miFormulario.cleaned_data
                servicio = Tipo_Servicio(nombre=data["nombre"], evento=data["evento"], email=data["email"], tipo_servicio=data["tipo_servicio"], telefono=data["telefono"])
                servicio.save()
                return render(req, "inicio.html")
            else:
                "Complete correctamente el campo e-mail"
                miFormulario.add_error("email", "El campo de correo electrónico debe contener '@'.")
        
    else:
        miFormulario = ServicioFormulario()
    
    return render(req, "servicioFormulario.html", {"miFormulario": miFormulario})
def busquedaEvento(req):
    return render(req, "busquedaEvento.html")


def buscar(req: HttpRequest):
    
    if req.GET["evento"]:
        evento = req.GET["evento"]
        servicio = Tipo_Servicio.objects.filter(evento__icontains = evento)
        return render(req, "resultadoBusqueda.html", {"nombres": servicio})
    else:
        return HttpResponse(f"Debe agregar un evento")
    
def ListaClientes(req):
        
    clientes = Cliente.objects.all()
    return render(req, "ListaClientes.html", {"clientes": clientes})


def ListaLugares(req):
        
    lugares = Lugar_Evento.objects.all()
    return render(req, "ListaLugares.html", {"lugares": lugares})


def ListaTrabajos(req):
        
    trabajos = Trabajos_entregar.objects.all()
    return render(req, "ListaTrabajos.html", {"trabajos": trabajos})

def Listashows(req):
        
    trabajos = Trabajos_entregar.objects.all()
    return render(req, "ListaTrabajos.html", {"trabajos": trabajos})

def ListaLugares(req):
        
    lugares = Lugar_Evento.objects.all()
    return render(req, "ListaLugares.html", {"lugares": lugares})

@login_required
def BuscarClientes(req):
    
    return render(req, "BusquedaClientes.html")

@login_required
def BuscarCli(req):
    nombre = req.GET.get('nombre')  # Utiliza req.GET.get() para obtener el valor del parámetro 'nombre'
    
    if nombre:
        try:
            nombre = Cliente.objects.get(nombre=nombre)
            return render(req, 'ResultadoBusquedaClientes.html', {'nombre': nombre})
        except Cliente.DoesNotExist:
            return HttpResponse('No hay clientes con ese nombre')

def buscarCli(req: HttpRequest):

    if req.GET["camada"]:
        nombre = req.GET["camada"]
        apeliido = Cliente.objects.filter(camada__icontains=camada)
        return render(req, "resultadosBusqueda.html", {"cursos": cursos})
    else:
        return HttpResponse(f"Debe agregar una camada")

      
def clienteFormulario(req):
    print('method', req.method)
    print('POST',  req.POST)
    
    if req.method == 'POST':
        
        clienteFormulario = ClienteFormulario(req.POST)
    
        if clienteFormulario.is_valid():
            
            data = clienteFormulario.cleaned_data
            nombre = Cliente(nombre = data["nombre"], apellido = data["apellido"], email = data["email"], tipo_servicio = data["tipo_servicio"], telefono = data["telefono"])
            nombre.save()
            
            return render(req, "inicio.html")
        
    else:
        clienteFormulario = ClienteFormulario()
        return render(req, "ClienteFormulario.html",{"clienteFormulario": clienteFormulario})


def lugarFormulario(req):
    print('method', req.method)
    print('POST',  req.POST)
    
    if req.method == 'POST':
        
        lugarFormulario = LugarFormulario(req.POST)
    
        if lugarFormulario.is_valid():
            
            data = lugarFormulario.cleaned_data
            lugar = Lugar_Evento(lugar = data["lugar"], localidad = data["localidad"], email = data["email"], salon = data["salon"])
            lugar.save()
            
            return render(req, "inicio.html")
        
    else:
        lugarFormulario = LugarFormulario()
        return render(req, "LugarFormulario.html",{"lugarFormulario": lugarFormulario})

def trabajoFormulario(req):
    print('method', req.method)
    print('POST',  req.POST)
    
    if req.method == 'POST':
        
        trabajoFormulario = TrabajoFormulario(req.POST)
    
        if trabajoFormulario.is_valid():
            
            data = trabajoFormulario.cleaned_data
            trabajo = Trabajos_entregar(trabajo = data["trabajo"], fecha_entrega = data["fecha_entrega"], entregado = data["entregado"], link = data["link"], email = data["email"])
            trabajo.save()
            
            return render(req, "inicio.html")
        
    else:
        trabajoFormulario = TrabajoFormulario()
        return render(req, "TrabajoFormulario.html",{"trabajoFormulario": trabajoFormulario})

def eliminarClientes(req, id):
    
    if req.method == 'POST':
        
        cliente = Cliente.objects.get (id=id)
        cliente.delete()
        
        clientes = Cliente.objects.all()
        return render(req, "ListaClientes.html", {"clientes": clientes})

##############################

#def editar_clientes(req,id):
    
#     nombre = Cliente.objects.get(id=id)
    
#     if req.method == 'POST':
    
#         if clienteFormulario.is_valid():
            
#             data = clienteFormulario.cleaned.data
#             nombre.nombre = data["nombre"]
#             nombre.apellido = data["apellido"]
#             nombre.email = data["email"] 
#             nombre.save()
            
#             return render(req, "inicio.html")
#     else:
        
#         clienteFormulario = ClienteFormulario(initial={
#             "nombre": nombre.nombre,
#             "apellido": nombre.apellido,
#             "email": nombre.email,
            
#         })
#         return render(req, "EditarClientes.html",{"clienteFormulario": clienteFormulario, "id": nombre})
##############


class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = "cliente_list.html"
    context_object_name = "clientes"
    
class ClienteDetail(DetailView):
    model = Cliente
    template_name = "cliente_detail.html"
    fields = ['nombre', 'apellido', 'email', 'tipo_servicio', 'telefono']
    success_url = '/AppFinal/'
    
           
# class ClienteCreate(CreateView):
#     model = Cliente
#     template_name = "cliente_create.html"
#     fields = ['nombre', 'apellido', 'email', 'tipo_servicio', 'telefono']
#     context_object_name = "cliente"
#     success_url = '/AppFinal/'

class ClienteCreate(CreateView):
    model = Cliente
    template_name = "cliente_create.html"
    fields = ['nombre', 'apellido', 'email', 'tipo_servicio', 'telefono']
    context_object_name = "cliente"
    success_url = '/AppFinal/'

    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']

        # Verificar si ya existe un cliente con el mismo nombre y apellido
        if Cliente.objects.filter(nombre=nombre, apellido=apellido).exists():
            # Si existe, muestra un mensaje de error
            form.add_error(None, 'Ya existe un cliente con el mismo nombre y apellido.')
            return self.form_invalid(form)
        
        return super().form_valid(form)
    
    
    
        
class ClienteUpdate(UpdateView):
    model = Cliente
    template_name = "cliente_update.html"
    fields = ('nombre', 'apellido', 'email', 'tipo_servicio','telefono')
    success_url = '/AppFinal/cliente-lista'
    context_object_name = "cliente"


class ClienteDelete(DeleteView):
    model = Cliente
    template_name = "cliente_delete.html"
    context_object_name = "cliente"
    success_url = '/AppFinal/cliente-lista'
    
    
##########################
def loginView(req):

    if req.method == 'POST':

        miFormulario = AuthenticationForm(req, data=req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username=usuario, password=psw)
            if user:
                login(req, user)
                return render(req, "inicio.html", {"mensaje": f"Bienvenido {usuario}!"})
            
        return render(req, "inicio.html", {"mensaje": f"Datos incorrectos"})
    else:
        miFormulario = AuthenticationForm()
        return render(req, "login.html", {"miFormulario": miFormulario})
    
def register(req):

    if req.method == 'POST':

        miFormulario = UserCreationForm(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            usuario = data["username"]
            miFormulario.save()
            return render(req, "inicio.html", {"mensaje": f"Usuario {usuario} creado con éxito!"})

        return render(req, "inicio.html", {"mensaje": f"Formulario invalido"})
            
    else:
        miFormulario = UserCreationForm()
        return render(req, "registro.html", {"miFormulario": miFormulario})

def editar_perfil(req):

    usuario = req.user
    if req.method == 'POST':

        miFormulario = UserEditForm(req.POST, instance=req.user)

        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.set_password(data["password1"])
            usuario.save()

            return render(req, "inicio.html", {"mensaje": "Datos actualizados con éxito!"})
        else:
            return render(req, "editarPerfil.html", {"miFormulario": miFormulario})

    else:
        miFormulario = UserEditForm(instance=usuario)
        return render(req, "editarPerfil.html", {"miFormulario": miFormulario})
    
def agregar_avatar(req):

    if req.method == 'POST':

        miFormulario = AvatarFormulario(req.POST, req.FILES)

        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data

            avatar = Avatar(user=req.user, imagen=data["imagen"])

            avatar.save()

            return render(req, "inicio.html", {"mensaje": "Avatar actualizados con éxito!"})

    else:
        miFormulario = AvatarFormulario()
        return render(req, "agregarAvatar.html", {"miFormulario": miFormulario})
    
@login_required  
def resultado_busqueda_clientes(request):
    nombre = request.GET.get('nombre', '')  # Obtiene el valor del parámetro 'nombre' desde la URL
    clientes = Cliente.objects.filter(nombre__startswith=nombre[:4])  # Realiza la búsqueda en la base de datos

    return render(request, 'resultado_busqueda_clientes.html', {'clientes': clientes})
    
# def mostrar_repositorio_de_imagenes(rutas_de_imagenes):
#     """
#     Muestra un repositorio de imágenes en una cuadrícula.

#     Args:
#     - rutas_de_imagenes (list): Una lista de rutas de archivos de imágenes.

#     """
#     num_imagenes = len(rutas_de_imagenes)
#     if num_imagenes == 0:
#         print("El repositorio está vacío.")
#         return

#     # Calcula el número de filas y columnas para la cuadrícula.
#     num_filas = int(num_imagenes ** 0.5)
#     num_columnas = (num_imagenes // num_filas) + (1 if num_imagenes % num_filas != 0 else 0)

#     # Configura el tamaño de la figura y crea la cuadrícula.
#     plt.figure(figsize=(12, 8))

#     for i, ruta_imagen in enumerate(rutas_de_imagenes):
#         plt.subplot(num_filas, num_columnas, i + 1)
#         imagen = mpimg.imread(ruta_imagen)
#         plt.imshow(imagen)
#         plt.axis('off')

#     plt.tight_layout()
#     plt.show()

# # Ejemplo de uso:
# rutas_de_imagenes = ['imagen1.jpg', 'imagen2.jpg', 'imagen3.jpg']
# mostrar_repositorio_de_imagenes(rutas_de_imagenes)

def mostrar_video(request):
    enlace_youtube = "https://www.youtube.com/watch?v=Ax08JRAMZGA"  # Reemplaza con el enlace de tu video de YouTube
    return render(request, 'video_template.html', {'enlace_youtube': enlace_youtube})

@login_required
def menuadmin(req):
    
    return render(req, "menuadmi.html")