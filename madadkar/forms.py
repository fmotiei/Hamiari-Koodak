import datetime
from django import forms
from django.contrib.auth.models import User


class SignUpInitialMadadju(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SignUpInitial, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ( 'first_name', 'last_name', 'email')

class SignUpForm(SignUpInitialMadadju):
    address = forms.CharField(required=False,
            max_length=2000,
            label='آدرس محل زندگی ',
            widget=forms.Textarea(attrs={'class':'form-control','name':'address'}),help_text=' پر کردن خانه‌های ستاره دار الزامی است!'
        )
    phone_number = forms.CharField( required=False, label='تلفن تماس ', widget=forms.TextInput(
            attrs={'type': 'text', 'class': "form-control", 'placeholder': "تلفن به همراه کد شهر", 'name':'phone_number'}))
    school = forms.CharField(required=False,
            max_length=50,
            label='مدرسه محل تحصیل ',
            widget=forms.TextInput(attrs={'type': 'text','class':'form-control', 'name':'school'}
        ))
    GPA = forms.IntegerField(min_value=0, max_value=20, required=True,widget=forms.Textarea(attrs={'type':'number', 'class': 'form-control',    'name' : "GPA",
    'placeholder' : "معدل" ,         'id':"GPA",}))

    OPTIONS = (
        ("AUT", "Austria"),
        ("DEU", "Germany"),
        ("NLD", "Neitherlands"),
    )
    paaye=  forms.MultipleChoiceField(choices=OPTIONS,widget=forms.SelectMultiple(attrs={'type':'number', 'class': 'form-control',    'name' : "paaye",}))

    class Meta(SignUpInitialMadadju.Meta):
        fields = SignUpInitialMadadju.Meta.fields + ('phone_number',) + ('school',)+('GPA',)+('paaye',) + ('address',)


class taghireNiazForm(forms.Form):
    mablagh = forms.IntegerField(min_value=0, max_value=99999999, required=True,widget=forms.Textarea(attrs={'type':'number', 'class': 'form-control',    'name' : "mablagh",
    'placeholder' : "مبلغ" ,         'id':"mablagh",}))
