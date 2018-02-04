import datetime
from django import forms
from django.contrib.auth.models import User

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
    phone_number = forms.EmailField(required=False, label='تلفن تماس ', widget=forms.TextInput(
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

