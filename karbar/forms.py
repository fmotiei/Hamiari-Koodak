import datetime
from django import forms
from django.contrib.auth.models import User
from karbar.models import Payam


class EditProfileForm(forms.Form):
    first_name = forms.CharField(required=False, label='نام', widget=forms.TextInput(
        attrs={'class': 'form-control', 'name': 'first_name', 'placeholder': 'نام'}))
    last_name = forms.CharField(required=False, label='نام خانوادگی', widget=forms.TextInput(
        attrs={'class': 'form-control', 'name': 'last_name', 'placeholder': 'نام خانوادگی'}))
    current_password = forms.CharField(required=True, label='پسورد فعلی',
                                       widget=forms.TextInput(
                                           attrs={'class': 'form-control', 'name': 'current_password', 'placeholder': '* گذرواژه',
                                                  'type': 'password'}))
    new_password = forms.CharField(required=False, label='',
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'name': 'new_password', 'placeholder': 'گذرواژه جدید',
                                              'type': 'password'}))
    re_new_password = forms.CharField(required=False, label='',
                                      widget=forms.TextInput(
                                          attrs={'class': 'form-control', 'name': 're_new_password',
                                                 'placeholder': 'تکرار گذرواژه جدید', 'type': 'password'}))


class SignInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def confirm_login_allowed(self, request):
        username = request.POST['username']
        print("users",User.objects.filter(username=username))
        if len(User.objects.filter(username=username)) == 0:
            return False
        return True


class SignUpInitial(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(SignUpInitial, self).__init__(*args, **kwargs)
    class Meta:
        model = User
        fields = ('username',  'first_name', 'last_name',  'email', 'password')
        labels = {'username':'نام کاربری',
                  'first_name':'نام',
                  'last_name':'نام خانوادگی',
                  'email':'پست الکترونیک',
                  'password':'گذرواژه'}


class SignUpForm(SignUpInitial):
    address = forms.CharField(required=False,
            max_length=2000,
            label='آدرس محل کار ',
            widget=forms.Textarea(attrs={'class':'form-control'}),help_text=' پر کردن خانه‌های ستاره دار الزامی است!'
        )
    phone_number = forms.CharField( required=False, label='تلفن تماس ', widget=forms.TextInput(
            attrs={'type': 'text', 'class': "form-control", 'placeholder': "تلفن به همراه کد شهر"}))
    bday = forms.DateField(required=False, label='تاریخ تولد', widget=forms.DateInput(attrs={'type':'date','class':'form-control'}))

    class Meta(SignUpInitial.Meta):
        fields = SignUpInitial.Meta.fields+('phone_number',)+('bday',)+('address',)
        help_texts = {
            'username': None,
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={'type': 'text', 'class': "form-control", 'id': "first_name", 'name': 'first_name',
                       'placeholder': "نام *"}),
            'last_name': forms.TextInput(
                attrs={'type': 'text', 'class': "form-control", 'id': "last_name", 'name': 'last_name',
                       'placeholder': "نام خانوداگی *"}),
            'email': forms.EmailInput(
            attrs={'type': 'text', 'class': "form-control", 'placeholder': "email *"}),
            'username':forms.TextInput(
                                   attrs={'type':'username' ,'class':"form-control",'placeholder': "نام کاربری *"}),
            'password': forms.TextInput(
            attrs={'type': 'password', 'class': "form-control",'placeholder':"گذرواژه*"})
        }#TODO validate konam ke first name vared shode

        error_messages = {
            'username': {
                'unique': ("این نام کاربری قبلا انتخاب شده است."),
            }
        }


class ErsalPayamInitial(forms.ModelForm):
    class Meta:
        model=Payam
        fields = ( 'onvan', 'matn')

class ErsalPayamForm(ErsalPayamInitial):
    reciever = forms.CharField(required=True , label='نام کاربری گیرنده ', widget=forms.TextInput(
            attrs={'type': 'text', 'class': "form-control", 'placeholder': "مثال: yeganeh"}))
    class Meta(ErsalPayamInitial.Meta):
        fields =('reciever',)+ ErsalPayamInitial.Meta.fields
