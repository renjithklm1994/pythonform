from django import forms
from .models import contacts
class contactForm(forms.ModelForm):
    """
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label='Your email')
    mobile = forms.CharField(label='Your phone',max_length=100)
    Message = forms.CharField(label='Your Message', max_length=500)
    """
    class Meta:
        model =contacts
        fields =['name','email','mobile','Message']