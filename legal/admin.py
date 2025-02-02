from django.contrib import admin
from . models import CaseEntry, CaseDetails

# Register your models here.

admin.site.register(CaseEntry)
admin.site.register(CaseDetails)