from django.shortcuts import render,redirect
from .models import Spend
from django.db.models import Sum
from .forms import SpendForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def delete_spend(request,id):
    spend=Spend.objects.get(pk=id)
    spend.delete()

    return redirect('spending')

@login_required
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
        return redirect('spending')

    return render(request,'spend/create_spend.html',{'form':form,'message':message})

@login_required
def spend(request,id):
    spend=None
    message=''
    try:
        spend=Spend.objects.get(id=id)
        if spend.user.id!=request.user.id:
            spend=None

            
        if request.method=='GET':
            form=SpendForm(instance=spend)
        
        if request.method=='POST':
            if request.POST.get('update'):
                form=SpendForm(request.POST,instance=spend)
                if form.is_valid():
                    spend=form.save(commit=False)
                    spend.user=request.user
                    spend.save()
                    message='更新成功'
            if request.POST.get('delete'):
                spend.delete()
                return redirect('spending')

    except Exception as e:
        print(e)
        message='更新失敗'
    return render(request,'spend/spend.html',{'spend':spend,'form':form,'message':message})

def spending(request):
    spends=None
    user=request.user
    if user.is_authenticated:
        spends=Spend.objects.filter(user=user).order_by('Creation')
    
    return render(request,'spend/spending.html',{'spends':spends})

