import datetime
from django import forms
from django.contrib.auth.models import User

class SignUpInitialMadadju(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SignUpInitial, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ( 'first_name', 'last_name', 'email')

class SignUpForm(SignUpInitial):
    class Meta(SignUpInitial.Meta):
        fields = SignUpInitial.Meta.fields + ('phone_number',) + ('school',) + ('address',)+('GPA',)+('paaye',)
