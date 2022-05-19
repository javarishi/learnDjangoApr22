'''
Created on 19-May-2022

@author: Rishi
'''
from django import forms
from products.models import Product
from django.core.exceptions import ValidationError

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title",
            "description", 
            "price",
            "feedback",
            "summary",
            ]
    
    
    def clean_title(self):
        in_title = self.cleaned_data.get("title")
        if "H2K" not in in_title:
            raise ValidationError("Title Must Contain H2K in it.")
        return in_title
        
        