
from django import forms

class afzayeshEtebar(forms.Form):
    mablagh = forms.IntegerField(min_value=0, max_value=99999999, required=True,widget=forms.Textarea(attrs={'type':'number', 'class': 'form-control',    'name' : "mablagh",
    'placeholder' : "مبلغ" ,         'id':"mablagh",}))
