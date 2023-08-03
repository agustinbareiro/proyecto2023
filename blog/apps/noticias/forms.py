from django import forms
from .models import Contacto
# comentario
from .models import Comentario


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = "__all__"


class Form_Mod(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ("texto",)
