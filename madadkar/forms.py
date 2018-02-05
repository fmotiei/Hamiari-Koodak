import datetime
from django import forms
from django.contrib.auth.models import User
from madadju.models import sharhe_tahsil, Niaz


class VirayeshTahsilForm(forms.ModelForm):
    tip=(
    ('GD', 'تغییر مثبت'),
    ('BD', 'تغییر منفی'))
    Taghirat=(
    ('gpa', 'تغییر چشمگیر در معدل'),
    ('olamp', 'شرکت در المپیاد دانش آموزی'),
    ('konkoor', 'شرکت در کنکور'),
    ('teacher', 'گزارش از معلم دانش آموز یا کادر مدرسه'),
    ('finals', 'گزارش امتحانات پایان سال'))
    Field_Taghir=forms.ChoiceField(choices=Taghirat, widget=forms.Select(attrs={'class':'form-control','name':'Field_Taghir'}))

    Type=forms.ChoiceField(choices=tip, widget=forms.Select(attrs={'class':'form-control','name':'Type'}))
    class Meta:
        model = sharhe_tahsil
        fields = ('onvan', 'sharh','Field_Taghir','Type')

class SignUpInitialMadadju(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SignUpInitialMadadju, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ( 'first_name', 'last_name', 'email')

class SignUpForm(SignUpInitialMadadju):
    address = forms.CharField(required=False,
            max_length=2000,
            label='آدرس محل زندگی ',
            widget=forms.TextInput(attrs={'class':'form-control','name':'address'}),help_text=' پر کردن خانه‌های ستاره دار الزامی است!'
        )
    phone_number = forms.CharField( required=False, label='تلفن تماس ', widget=forms.TextInput(
            attrs={'type': 'text', 'class': "form-control", 'placeholder': "تلفن به همراه کد شهر", 'name':'phone_number'}))
    school = forms.CharField(required=False,
            max_length=50,
            label='مدرسه محل تحصیل ',
            widget=forms.TextInput(attrs={'type': 'text','class':'form-control', 'name':'school'}
        ))
    GPA = forms.IntegerField(min_value=0, max_value=20, required=True,widget=forms.TextInput(attrs={'type':'number', 'class': 'form-control',    'name' : "GPA",
    'placeholder' : "معدل" ,         'id':"GPA",}))

    class Meta(SignUpInitialMadadju.Meta):
        fields = SignUpInitialMadadju.Meta.fields + ('phone_number',) + ('school',)+('GPA',) + ('address',)


class taghireNiazForm(forms.Form):
    mablagh = forms.IntegerField(min_value=0, max_value=99999999, required=True,widget=forms.Textarea(attrs={'type':'number', 'class': 'form-control',    'name' : "mablagh",
    'placeholder' : "مبلغ" ,         'id':"mablagh",}))

class afzoodanNiazForm(forms.ModelForm):

    noe = (
        ('yr', 'سالانه'),
        ('mo', 'ماهانه'))
    Type=forms.ChoiceField(choices=noe, widget=forms.Select(attrs={'class':'form-control','name':'Type'}))
    class Meta:
        model = Niaz
        fields = ('onvan', 'mablagh','Type','niazFori')
