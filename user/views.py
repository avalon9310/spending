from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def user_profile(request,id):
    user=None
    try:
        user=User.objects.get(pk=id)
    except Exception as e:
        print(e)
        
    return render(request,'user/profile.html',{'user':user})

def user_login(request):
    message=''
    if request.method=='POST':
        if request.POST.get('register'):
            return redirect('register')
        
        if request.POST.get('login'):
            username=request.POST.get('username')
            password=request.POST.get('password')
            if username=='' or password=='':
                message='帳號或密碼不能為空!'
            else:
                #登入動作
                user=authenticate(request,username=username,password=password)
                print(user)
                if not user:
                    if User.objects.filter(username=username):
                        message='密碼錯誤!'
                    else:
                        message='帳號錯誤!'
                else:
                    login(request,user)
                    message='登入成功'
                    return redirect('spending')
                
    return render(request,'user/login.html',{'message':message})

# Create your views here.
def user_register(request):
    message=''
    form=UserCreationForm()
    if request.method=='GET':
        print('GET')

    if request.method=='POST':
        try:
            username=request.POST.get('username')
            email=request.POST.get('email')
            password1=request.POST.get('password1')
            password2=request.POST.get('password2')
            print(username,password1,password2)

            if username=='':
                message='請輸入帳號'
            elif password1=='':
                message='請輸入密碼'
            elif password2=='':
                message='請再次輸入密碼'
            elif len(password1)<8:
                message='密碼需至少8碼!'
            elif password1!=password2:
                message='兩次密碼不同!'
            else:
                if User.objects.filter(username=username).exists():
                    message='此帳號已註冊!'
                else:
                    user=User.objects.create_user(username=username,password=password1,email=email)
                    user.save()
                    login(request,user)
                    message='註冊成功'
                    return redirect('spending')
        except Exception as e:
            print(e)
            message='註冊失敗'

    
    return render(request,'user/register.html',{'form':form,'message':message})