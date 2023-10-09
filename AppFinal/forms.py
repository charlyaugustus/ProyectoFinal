from django import forms
from .models import Avatar
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User



class ServicioFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=40)
    evento = forms.CharField(max_length=40)
    email = forms.CharField(max_length=40)
    tipo_servicio = forms.CharField(max_length=40)
    telefono = forms.CharField(max_length=40)
    
    
class ClienteFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email= forms.EmailField()
    tipo_servicio = forms.CharField(max_length=40)
    telefono = forms.CharField(max_length=40)
    
class LugarFormulario(forms.Form):
    lugar = forms.CharField(max_length=40)
    localidad = forms.CharField(max_length=40)
    email = forms.EmailField()
    salon = forms.CharField(max_length=40)
    
class CustomBooleanChoiceWidget(forms.RadioSelect):
    choices = [(True, 'Entregado'), (False, 'No entregado')]

class TrabajoFormulario(forms.Form):
    trabajo = forms.CharField(max_length=40)
    fecha_entrega = forms.DateField()
    entregado = forms.ChoiceField(choices=[(True, 'Entregado'), (False, 'No entregado')], widget=CustomBooleanChoiceWidget)
    link = forms.CharField(max_length=256)
    email = forms.EmailField()
    
class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields = ("email", "first_name", "last_name", "password1", "password2")

    def clean_password2(self):

        print(self.cleaned_data)

        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden!!!!")
        return password2
    
class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ("imagen",)


