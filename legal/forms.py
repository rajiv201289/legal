from django import forms
from . models import CaseDetails, CaseEntry

class CaseEntryForm(forms.ModelForm):
    class Meta:
        model = CaseEntry
        fields = ['case_no']
        labels = {'case no':''}