from django.shortcuts import render, redirect
from . import models
from .models import UserForm

# Create your views here.

# user_list = []


def index(request):
    pass
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     # 存入数据库
    #     models.UserInfo.objects.create(user=username,pwd=password)
    # # 数据库读取
    # user_list = models.UserInfo.objects.all()
    # print(user_list)
    return render(request, 'index.html')

def login(request):
    if request.session.get('is_login',None):
        return redirect('/index')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.UserForm.objects.get(name=username)
                if user.password == password:
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login.html', locals())

    login_form = UserForm()
    return render(request, 'login.html', locals())

def register(request):
    pass
    return render(request, 'register.html')

def logout(request):
    pass
    return redirect(request, '/index/')
