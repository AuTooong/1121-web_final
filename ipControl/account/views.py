from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import User
from django.template import loader
from django.http import HttpResponse
from ipControl.views import index

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username, password=password)
        except:
            user = None

        if user is not None:
            print("登入成功")
            # 登入成功後的重定向，可以根據需求修改
            return redirect('/')
        else:
            # 登入失敗的處理，例如顯示錯誤訊息
            print("登入失敗")
            error_message = "登入失敗，請檢查使用者名稱和密碼。"
            return render(request, 'login.html', {'error_message': error_message})

    # 如果是 GET 請求，顯示登入表單
    return render(request, 'login.html')
