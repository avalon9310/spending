from django.shortcuts import render

# Create your views here.

def spend(request):
    return render(request,'spend/spend.html')