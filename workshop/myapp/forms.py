from dataclasses import fields
from tkinter import Widget
from django import forms
from myapp.models import *
class patient_details(forms.ModelForm):
    class Meta:
        model=home
        fields="__all__"
        Widget={

        }