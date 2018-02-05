from django import forms

class taghirMadadkarForm(forms.Form):
    sharh = forms.CharField( required=True,widget=forms.Textarea(attrs={'type':'text', 'class': 'form-control',    'name' : "sharh",
    'placeholder' : "توضیحات" ,       }))
