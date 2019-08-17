from django import forms
from .models import product

class productform(forms.Form):
    No=forms.IntegerField()
    Name=forms.CharField(max_length=10)
    Catagory=forms.CharField(max_length=10)
    Email=forms.EmailField()
    Contact=forms.IntegerField()
    
class aboutform(forms.ModelForm):
    class Meta:
        models=product
        fields=['No','Name','Catagory','Email','Contact']