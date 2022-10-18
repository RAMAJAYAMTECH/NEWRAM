from django import forms
from django.forms import fields
from app.models import Messagebox,getintouch


class Form1(forms.ModelForm):
    class Meta:
       model = Messagebox
       fields = '__all__'

class Form2(forms.ModelForm):
    class Meta:
       model = getintouch
       fields = '__all__'