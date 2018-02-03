from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
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
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                message = 'ثبت نام شما با خطا مواجه شد! دوباره تلاش کنید.'
                return render(request, template, {'form': form, 'message': message})

            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()

            login(request, user)
            Hamiar.objects.create(user=user, phone_number=phone_number, address=address)
            return HttpResponseRedirect(reverse("hamyar_panel")+"?success=1")  # this should be hamyar's own page
        else:
            return render(request, template, {'form': form})


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
