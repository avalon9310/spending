from django.forms import ModelForm
from .models import Spend


class SpendForm(ModelForm):
    class Meta:
        model = Spend
        fields=('title','text','amount','category')