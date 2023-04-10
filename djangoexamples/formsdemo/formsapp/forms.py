from django import forms
from .models import Contact

class Contactform(forms.ModelForm):
    class Meta:         #it contains all data
        model = Contact
        fields = [
            'name','email','content'
        ]