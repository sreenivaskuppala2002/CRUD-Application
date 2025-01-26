from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from . models import Records

class Registerform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']

class Insertform(ModelForm):
    class Meta:
        model=Records
        fields=['first_name','last_name','email','mobile','Address']



        