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
from karbar import moshtarak
import hamiar
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
        if form.is_valid():
            last_name = form.cleaned_data['last_name']
            first_name = form.cleaned_data['first_name']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            if User.objects.filter(username=username).exists():
                return render(request, template, {'form': form})

            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()
            ukarbar=UserKarbar.objects.create(user=user, phone_number=phone_number, address=address)
            staff=staff_members.objects.create(stafID=ukarbar,pardakhti=0,dariafti=0 )
            hamiar.models.Hamiar.objects.create(staffID=staff )
            login(request, user)
            return render(request, '/hamiar/', {'form': form, 'utype' : 'hamiar'
        , 'progress': karbar.darbare_ma.progress()
        , 'username':''
        , 'roydadha' : {} })
            # return HttpResponseRedirect(reverse("hamyar_panel")+"?success=1")  # this should be hamyar's own page
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

def show_register_success(request):
    return render(request,"karbar/regiset_success.html")
