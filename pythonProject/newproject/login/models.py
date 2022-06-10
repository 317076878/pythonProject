from django.db import models
from django import forms
from captcha.fields import CaptchaField

# Create your models here.

class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')

class UserInfo(models.Model):
    '''用户表'''

    gender = (
        ('male', '男'),
        ('famale', '女'),
    )
    user = models.CharField(max_length=32,unique=True)
    pwd = models.CharField(max_length=32)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32,choices=gender,default='男')
    c_time = models.DateTimeField(auto_now_add=True)
    tel = models.CharField(max_length=32)
