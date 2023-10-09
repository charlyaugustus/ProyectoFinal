from django.urls import path
from .views import *
from django.contrib.auth.views import *



urlpatterns = [
    path("listaServicios/", listaServicios, name="ListaServicios"),
    path("", inicio, name="Inicio"),
    path('nuestrosclientes/', clientes, name="NuestrosClientes"),
    path("lugar/", lugar, name="Lugar_Evento"),
    path("entregables/", fecha_entregar, name="Fecha de Entrega"),
    path("servicio-formulario/", servicioFormulario, name="ServicioFormulario"),
    path("busqueda-evento/", busquedaEvento, name="BusquedaEvento"),
    path("listaclientes/", ListaClientes, name="ListaClientes"),
    path("buscar/", buscar, name="Buscar"),
    path("listalugares/", ListaLugares, name="ListaLugares"),
    path("listatrabajos/", ListaTrabajos, name="ListaTrabajos"),
    path("busqueda-clientes/", BuscarClientes, name="BusquedaClientes"),
    path("busquedando-cli/", BuscarCli, name="ResultadoBusquedaClientes"),
    path("cliente-formulario/", clienteFormulario, name="ClienteFormulario"),
    path("lugar-formulario/", lugarFormulario, name="LugarFormulario"),
    path("trabajo-formulario/", trabajoFormulario, name="TrabajoFormulario"),
    path("eliminar-cliente/<int:id>", eliminarClientes, name="EliminarClientes"),
    #path("editar-cliente/<int:id>", editar_clientes, name="EditarClientes"),
    path("cliente-lista/", ClienteList.as_view(), name="ClienteLista"),
    path("cliente-detail/<pk>", ClienteDetail.as_view(), name="ClienteDetalle"),
    path("cliente-crear/", ClienteCreate.as_view(), name="ClienteCrear"),
    path('cliente-update/<pk>', ClienteUpdate.as_view(), name="ClienteUpdate"),
    path("cliente-delete/<pk>", ClienteDelete.as_view(), name="ClienteDelete"),
    path('login/', loginView, name="Login"),
    path('register/', register, name="Registrar"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path('agregar-avatar/', agregar_avatar, name="AgregarAvatar"),
    path('editar-pefil/', editar_perfil, name="EditarPefil"),
    path('mostrar_video/', mostrar_video, name='mostrar_video'),
    path('menuadmin/', menuadmin, name='mostrar_menu'),
    path('shows/', mostrar_eventos, name='shows'),
    path('about/', about, name='About'),
    

    
   
   
    

   
    
    
    
   
    
    
]


    
    
    
   
    
    


