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
import modir.views

urlpatterns = [
    url(r'ahdaf/', modir.views.show_ahdaf),
    url(r'ashnai/', modir.views.show_ashnai),
    url(r'ersal_payam/', modir.views.show_ersal_payam),
    url(r'ezafe_kardan_amr_kheyrie_motefareghe/', modir.views.show_ezafe_kardan_amr_kheyrie_motefareghe),
    url(r'list_omur_kheyrie/', modir.views.show_list_omur_kheyrie),
    url(r'modir/', modir.views.show_modir),
    url(r'moshahede_etelat_mali_karbaran/', modir.views.show_moshahede_etelat_mali_karbaran),
    url(r'moshahede_hamyaran_dar_entezar_taeid/', modir.views.show_moshahede_hamyaran_dar_entezar_taeid),
    url(r'moshahede_list_koodakan/', modir.views.show_moshahede_list_koodakan),
    url(r'moshahede_list_niazhaye_fori_taminnashode/', modir.views.show_moshahede_list_niazhaye_fori_taminnashode),
    url(r'moshahede_madadjuyan_dar_entezar_madadkar/', modir.views.show_moshahede_madadjuyan_dar_entezar_madadkar),
    url(r'payam_daryafti/', modir.views.show_payam_daryafti),
    url(r'profile/', modir.views.show_profile),
    url(r'roydadha/', modir.views.show_roydadha),
    url(r'sabtename_madadkar/', modir.views.show_sabtename_madadkar),
    url(r'sabtename_modir_karshenas/', modir.views.show_sabtename_modir_karshenas),
    url(r'sakhtar_sazmani/', modir.views.show_sakhtar_sazmani),
    url(r'sandoghe_payamhaye_daryafti/', modir.views.show_sandoghe_payamhaye_daryafti),
    url(r'sandoghe_payamhaye_ersali/', modir.views.show_sandoghe_payamhaye_ersali),
    url(r'amaliat_movafagh/', modir.views.show_amaliat_movafagh),
    url(r'moshahede_tarakonesh_haye_mali/', modir.views.show_moshahede_tarakonesh_haye_mali),
    url(r'afzayesh_etebar/', modir.views.show_afzayesh_etebar),
    url(r'madadju_profile/', modir.views.show_madadju_profile),

    url(r'^$', modir.views.show_modir),
]
