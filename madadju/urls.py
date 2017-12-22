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
import madadju.views

urlpatterns = [
    url(r'afzayesh_etebar/', madadju.views.show_afzayesh_etebar),
    url(r'ahdaf/', madadju.views.show_ahdaf),
    url(r'ashnai/', madadju.views.show_ashnai),
    url(r'darkhast_taghir_madadkar/', madadju.views.show_darkhast_taghir_madadkar),
    url(r'ersal_payam/', madadju.views.show_ersal_payam),
    url(r'madadju/', madadju.views.show_madadju),
    url(r'payam_daryafti/', madadju.views.show_payam_daryafti),
    url(r'payam_ersali/', madadju.views.show_payam_ersali),
    url(r'moshahede_tarakonesh_haye_mali/', madadju.views.show_moshahede_tarakonesh_haye_mali),
    url(r'profile/', madadju.views.show_profile),
    url(r'roydadha/', madadju.views.show_roydadha),
    url(r'sakhtar_sazmani/', madadju.views.show_sakhtar_sazmani),
    url(r'sandoghe_payamhaye_daryafti/', madadju.views.show_sandoghe_payamhaye_daryafti),
    url(r'sandoghe_payamhaye_ersali/', madadju.views.show_sandoghe_payamhaye_ersali),
    url(r'amaliat_movafagh/', madadju.views.show_amaliat_movafagh),
    url(r'^$', madadju.views.show_madadju),
]
