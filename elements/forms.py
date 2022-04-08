from django import forms
from django.core.validators import MinLengthValidator,EmailValidator
from .models import Category, Element, Type

class ElementForm(forms.Form):

    title = forms.CharField(label="Título", max_length=255, min_length=3 ) 
    description = forms.CharField(label='Descripción', initial='Tu increible post por aquí', widget=forms.Textarea, validators=[MinLengthValidator(2, message='Muy corto! (minino %(limit_value)d) actual %(show_value)d ')] )
    price = forms.DecimalField(label="Precio", required=False, max_digits=5, decimal_places=2)    
    type = forms.ModelChoiceField(label='Tipo', queryset=Type.objects.all(), initial=2)
    category = forms.ModelChoiceField(label='Categoría', queryset=Category.objects.all())