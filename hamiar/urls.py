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
    2. Add a URL to urlpatterns:  url(r'blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin
import hamiar.views

urlpatterns = [
    url(r'^afzayesh_etebar/$', hamiar.views.show_afzayesh_etebar),
    url(r'^ahdaf/$', hamiar.views.show_ahdaf),
    url(r'^ashnai/$', hamiar.views.show_ashnai),
    url(r'^ersal_payam/$', hamiar.views.show_ersal_payam),
    url(r'^hemayat_az_moasese/$', hamiar.views.show_hemayat_az_moasese),
    url(r'^hemayat_az_niaz/$', hamiar.views.show_hemayat_az_niaz),
    url(r'^moshahede_niaz_haye_taht_hemayat/$', hamiar.views.show_moshahede_niaz_haye_taht_hemayat),
    url(r'^moshahede_tarakonesh_haye_mali/$', hamiar.views.show_moshahede_tarakonesh_haye_mali),
    url(r'^niaz_haye_tamin_nashode/$', hamiar.views.show_niaz_haye_tamin_nashode),
    url(r'^niaz_haye_madadju/$', hamiar.views.show_niaz_haye_madadju),
    url(r'^payam_daryafti/$', hamiar.views.show_payam_daryafti),
    url(r'^payam_ersali/$', hamiar.views.show_payam_ersali),
    url(r'^profile/$', hamiar.views.show_profile),
    url(r'^profile_madadju/$', hamiar.views.show_profile_madadju),
    url(r'^roydadha/$', hamiar.views.show_roydadha),
    url(r'^sakhtar_sazmani/$', hamiar.views.show_sakhtar_sazmani),
    url(r'^sandoghe_payamhaye_daryafti/$', hamiar.views.show_sandoghe_payamhaye_daryafti),
    url(r'^sandoghe_payamhaye_ersali/$', hamiar.views.show_sandoghe_payamhaye_ersali),
    url(r'^Enseraf/$', hamiar.views.Enseraf, name="Enseraf"),
    url(r'^amaliat_movafagh/$', hamiar.views.show_amaliat_movafagh),
    url(r'^moshahede_list_koodakan/$', hamiar.views.show_moshahede_list_koodakan),
    url(r'^moshahede_list_niazhaye_fori_taminnashode/$', hamiar.views.show_moshahede_list_niazhaye_fori_taminnashode),
    url(r'^$', hamiar.views.show_hamiar,name="hamyar_panel"),
]
