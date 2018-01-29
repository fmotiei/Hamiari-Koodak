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
import madadkar.views

urlpatterns = [
    url(r'afzayesh_etebar/', madadkar.views.show_afzayesh_etebar),
    url(r'afzoudan_niaz/', madadkar.views.show_afzoudan_niaz),
    url(r'ahdaf/', madadkar.views.show_ahdaf),
    url(r'ashnai/', madadkar.views.show_ashnai),
    url(r'ersal_payam/', madadkar.views.show_ersal_payam),
    url(r'moshahede_madadjuyan_taht_kefalat/', madadkar.views.show_moshahede_madadjuyan_taht_kefalat),
    url(r'moshahede_madadjuyan_dar_entezar_madadkar/', madadkar.views.show_moshahede_madadjuyan_dar_entezar_madadkar),
    url(r'moshahede_tarakonesh_haye_mali/', madadkar.views.show_moshahede_tarakonesh_haye_mali),
    url(r'niaz_haye_tamin_nashode/', madadkar.views.show_niaz_haye_tamin_nashode),
    url(r'niaz_haye_madadju/', madadkar.views.show_niaz_haye_madadju),
    url(r'niaz_haye_madadju_bi_kefalat/', madadkar.views.show_niaz_haye_madadju_bi_kefalat),
    url(r'niaz_haye_tamin_nashode_fori/', madadkar.views.show_niaz_haye_tamin_nashode_fori),
    url(r'payam_daryafti/', madadkar.views.show_payam_daryafti),
    url(r'payam_ersali/', madadkar.views.show_payam_ersali),
    url(r'payam_entezar/', madadkar.views.show_payam_entezar),
    url(r'profile/', madadkar.views.show_profile),
    url(r'profile_madadju/', madadkar.views.show_profile_madadju),
    url(r'profile_madadju_bi_kefalat/', madadkar.views.show_profile_madadju_bi_kefalat),
    url(r'roydad_ha/', madadkar.views.show_roydad_ha),
    url(r'sakhtar_sazmani/', madadkar.views.show_sakhtar_sazmani),
    url(r'sandoghe_payamhaye_daryafti/', madadkar.views.show_sandoghe_payamhaye_daryafti),
    url(r'sandoghe_payamhaye_ersali/', madadkar.views.show_sandoghe_payamhaye_ersali),
    url(r'sandoghe_payamhaye_entezar/', madadkar.views.show_sandoghe_payamhaye_entezar),
    url(r'amaliat_movafagh/', madadkar.views.show_amaliat_movafagh),
    url(r'sabte_naam_madadju/',madadkar.views.show_sabte_naam_madadju),
    url(r'virayesh_niaz/',madadkar.views.show_virayesh_niaz),
    url(r'vaziat_tahsili/',madadkar.views.show_vaziat_tahsili),
    url(r'moshahede_list_koodakan/', madadkar.views.show_moshahede_list_koodakan),
    url(r'moshahede_list_niazhaye_fori_taminnashode/', madadkar.views.show_moshahede_list_niazhaye_fori_taminnashode),
    url(r'^$', madadkar.views.show_madadkar),
]
