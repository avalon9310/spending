from django.shortcuts import render
from .models import Spend
from django.db.models import Sum
# Create your views here.

def spend(request,id):
    spend=None
    try:
        spend=Spend.objects.get(pk=id)
    except Exception as e:
        print(e)
    return render(request,'spend/spend.html',{'spend':spend})

def spending(request):
    spends=None
    user=request.user
    if user.is_authenticated:
        spends=Spend.objects.filter(user=user)
    
    return render(request,'spend/spending.html',{'spends':spends})

