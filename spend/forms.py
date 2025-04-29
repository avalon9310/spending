from django.forms import ModelForm
from .models import Spend
from django import forms


class SpendForm(ModelForm):
    class Meta:
        model = Spend
        fields=('title','text','Creation_date','amount','category')
     