"""calculus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin
import karbar.views

urlpatterns = [
    url(r'ahdaf/', karbar.views.show_ahdaf),
    url(r'ashnai/', karbar.views.show_ashnai),
    url(r'sakhtar_sazmani/', karbar.views.show_sakhtar_sazmani),
    url(r'moshahede_list_koodakan/', karbar.views.show_moshahede_list_koodakan),
    url(r'moshahede_list_niazhaye_fori_taminnashode/', karbar.views.show_moshahede_list_niazhaye_fori_taminnashode),
    url(r'profile/', karbar.views.show_profile),
    url(r'sabtename_hamyar/', karbar.views.show_sabtename_hamyar),
    url(r'^$', karbar.views.show_profile, name='hamiar'), #TODO in name ro alaki gozashtam ta az sign up redirect kone inja
]
