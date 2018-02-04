from django.db import models
from .models import *
import karbar

# Create your models here.


class ModirArshad(models.Model):
    staffID =  models.OneToOneField(karbar.models.staff_members, on_delete=models.CASCADE, default='')
    hoghugh = models.PositiveIntegerField()
    def username(self):
        return self.staffID.stafID.user.username


class ModirKarshenas(models.Model):
    staffID =  models.OneToOneField(karbar.models.staff_members, on_delete=models.CASCADE, default='')
    hoghugh = models.PositiveIntegerField()
    def username(self):
        return self.staffID.stafID.user.username

