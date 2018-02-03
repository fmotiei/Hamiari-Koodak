from django import forms
from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse
import karbar.darbare_ma
from django.views.decorators.csrf import csrf_exempt
from .forms import SignUpForm
from .models import *

# Create your views here.
from karbar import moshtarak
from madadju.models import Madadju, Niaz

def show_profile(request):
    return moshtarak.show_user(request,'karbar')

def show_sabtename_hamyar(request):
    template = 'karbar/sabtename_hamyar.html'
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, template, {'form': form})

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        args = {'form': form}
        if form.is_valid():
            new_hamyar = hamiar.models.Hamyar()
            new_hamyar.first_name = form.cleaned_data['first_name']
            new_hamyar.last_name = form.cleaned_data['last_name']
            new_hamyar.phone_number = form.cleaned_data['phone_number']
            new_hamyar.address = form.cleaned_data['address']
            new_hamyar.email = form.cleaned_data['email']
            new_hamyar.password = form.cleaned_data['password']
            new_hamyar.username = form.cleaned_data['username']
            new_hamyar.save()
            return redirect('hamiar') #TODO inja redirect kone to safhe sing in
        else:
            message='ثبت نام شما با خطا مواجه شد! دوباره تلاش کنید.'
            return render(request, template, {'form': form,'message':message})


def show_ahdaf(request):
    return moshtarak.show_ahdaf(request,'karbar')

def show_ashnai(request):
    return moshtarak.show_ashnai(request,'karbar')


def show_sakhtar_sazmani(request):
    return moshtarak.show_sakhtar_sazmani(request,'karbar')

def show_moshahede_list_koodakan(request):
    return moshtarak.show_moshahede_list_koodakan(request,'karbar')

def show_moshahede_list_niazhaye_fori_taminnashode(request):
    return moshtarak.show_moshahede_list_niazhaye_fori_taminnashode(request,'karbar')
