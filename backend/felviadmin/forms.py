from django import forms
from .models import Szak, Felvetelizo

class SzakForm(forms.ModelForm):
    class Meta:
        model = Szak
        fields = '__all__'
        #fields = ['mező1', 'mező2', 'mezőstb']

        widgets = {
            "szakNev" : forms.TextInput(attrs={'class': 'form-control'}),
            "tamogatott" : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
        labels = {
            "szakNev" : "Szakágazat neve ",
            "tamogatott" : "A szak költségtérítéses ",
        }

class FelvetelizoForm(forms.ModelForm):
    class Meta:
        model = Felvetelizo
        fields = '__all__'
        #fields = ['mező1', 'mező2', 'mezőstb']
        
        labels = {
            "nev" : "Felvételiző neve ",
            "szul_evszam" : "Születési évszám ",
            "pontszam" : "Megszerzett pontok száma ",
            "szak" : "Választott szak megnevezése ",
        }
        
        widgets = {
            "nev" : forms.TextInput(attrs={'class': 'form-control'}),
            "szul_evszam" : forms.NumberInput(attrs={'class': 'form-control'}),
            "pontszam" : forms.NumberInput(attrs={'class': 'form-control'}),
            "szak" : forms.Select(attrs={'class': 'form-select'}),
        }