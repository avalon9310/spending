from django.shortcuts import render
from .models import Spend
# Create your views here.

def spend(request):
    spends=Spend.objects.all()
    
    return render(request,'spend/spend.html',{'spends':spends})