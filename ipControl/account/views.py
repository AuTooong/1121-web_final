from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.template import loader
from django.http import HttpResponse
from ipControl.views import index
from django.contrib import messages

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request, username=username, password=password)

        if user is not None:
            print("登入成功")
            # 登入成功後的重定向，可以根據需求修改
            login(request, user)
            if request.POST.get('next') is not None:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')
        else:
            # 登入失敗的處理，例如顯示錯誤訊息
            print("登入失敗")
            error_message = "登入失敗，請檢查使用者名稱和密碼。"
            return render(request, 'login.html', {'error_message': error_message})

    # 如果是 GET 請求，顯示登入表單
    
    return render(request, 'login.html', {'next' : request.GET.get('next')})

def logout_view(request):
    logout(request)
    return redirect('/')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '註冊成功')
            return redirect('/')
        else:
            messages.error(request, '註冊失敗，請檢查輸入資料')
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})
