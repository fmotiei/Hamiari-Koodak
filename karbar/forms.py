import datetime
from django import forms
from hamiar.models import Hamiar
class SignUpForm(forms.Form):

        first_name = forms.CharField(required=True,label='نام ',widget=forms.TextInput(
                                   attrs={'type':'text' ,'class':"form-control" ,'id':"first_name", 'name':'first_name' ,'placeholder':"نام *" }))

        last_name = forms.CharField(required=True, label='نام خانوادگی ', widget=forms.TextInput(
            attrs={'type': 'text', 'class': "form-control", 'id': "last_name", 'name': 'last_name',
                   'placeholder': "نام خانوداگی *"}))

        email = forms.EmailField(required=True, label='پست الکترونیک ', widget=forms.TextInput(
            attrs={'type': 'text', 'class': "form-control", 'placeholder': "email *"}))
        username = forms.CharField(required=True,label='نام کاربری ',widget=forms.TextInput(
                                   attrs={'type':'text' ,'class':"form-control",'placeholder': "نام کاربری *"}))

        password = forms.CharField(required=True, label='گذرواژه ', widget=forms.TextInput(
            attrs={'type': 'text', 'class': "form-control",
                   'placeholder': "گذرواژه *"}))

        phone_number = forms.EmailField(required=False, label='تلفن تماس ', widget=forms.TextInput(
            attrs={'type': 'text', 'class': "form-control", 'placeholder': "تلفن به همراه کد شهر"}))
        bday = forms.DateField(required=False, label='تاریخ تولد', widget=forms.DateInput(attrs={'type':'date','class':'form-control'}))

        address = forms.CharField(required=False,
            max_length=2000,
            label='آدرس محل کار ',
            widget=forms.Textarea(attrs={'class':'form-control'}),
            help_text=' پر کردن خانه‌های ستاره دار الزامی است!'
        )

        def clean(self):
            cleaned_data = super(SignUpForm, self).clean()
            return cleaned_data

        def is_valid(self):
            print(Hamiar.objects.get(username=username))
            valid = super(SignUpForm, self).is_valid()
            if not valid:
                return valid

            username = self.cleaned_data['username']

            if len(Hamiar.objects.get(username=username)) > 0:
                self._errors['نام کاربری تکراری است'] = ''
                return False

            return True



