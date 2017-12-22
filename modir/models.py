from django.db import models
from django import forms
from django.core.validators import RegexValidator
from madadju.models import *
from madadkar.models import *
from hamiar.models import *
from karbar.models import *



# Create your models here.


class ModirArshad(staff_members):
    hoghugh = models.PositiveIntegerField()


class ModirKarshenas(staff_members):
    hoghugh = models.PositiveIntegerField()

