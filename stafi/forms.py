from django import forms
from .models import Profesori, Kurset, Subject, CustomUser
from django.contrib.auth.forms import UserCreationForm



class ProfesoriForm(forms.ModelForm):
    class Meta:
        model = Profesori
        fields = ( 'emri', 'mbiemri', 'cel', 'email')
        labels= {
            'emri': 'Name',
            'mbiemri':'Surname',
            'cel':'Cel',
            'email':'Email'
        }


wigets = {
    'emri': forms.TextInput(attrs={'class':'form-control'}),
    'mbiemri': forms.TextInput(attrs={'class':'form-control'}),
    'cel': forms.NumberInput(attrs={'class':'form-control'}),
    'email':forms.EmailInput(attrs={'class':'form-control'})
}

class KursetForm(forms.ModelForm):
    class Meta:
        model = Kurset
        fields= ('leksioni', 'petagogu', 'kredite')
        labels = {
            'leksioni': 'Lessions',
            'petagogu': 'Professor',
            'kredite': 'Credits',

        }


class SubjectFrom(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('name', 'description')
        labels = {
            'name':'Name',
            'description':'Description'
        }



class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2','email')
        labels={
            'username':'Username',
            'password1':'Password1',
            'password2':'Password2',
            'email':'Email'
        }


