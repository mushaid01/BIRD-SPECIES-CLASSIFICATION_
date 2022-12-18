from django import forms
  
class GeeksForm(forms.Form):
    geeks_field = forms.FileField()
from myapp.models import bird
class HotelForm(forms.ModelForm):
 
    class Meta:
        model = bird
        fields = ['hotel_Main_Img']