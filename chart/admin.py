from django.contrib import admin
from django.shortcuts import render
from django.http import Http404

# Register your models here.

from .models import Tempvalt

admin.site.register(Tempvalt)

