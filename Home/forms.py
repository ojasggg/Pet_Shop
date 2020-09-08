from django import forms
from Home.models import Contact,Registered

 

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

class RegisteredForm(forms.ModelForm):
    class Meta:
        model = Registered
        fields = "__all__"

    