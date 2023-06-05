from django.shortcuts import render
from .models import Spend
from django.db.models import Sum
from .forms import SpendForm
# Create your views here.

def create_spend(request):
    message=''
    form=SpendForm()
    if request.method=='POST':
        print(request.POST)
        form=SpendForm(request.POST)
        spend=form.save(commit=False)
        spend.user=request.user
        spend.save()
        message='建立成功'

    return render(request,'spend/create_spend.html',{'form':form,'message':message})

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

