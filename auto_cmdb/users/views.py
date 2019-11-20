from django.shortcuts import render
from django.contrib.auth.views import LogoutView  
from django.contrib.auth.views import LoginView  
from django.views.generic.edit import FormView
from django.urls import reverse,reverse_lazy
from users.users_forms import (
    UserRegisterForm,UserRegisterModelForm
)
from users.models import UsersProfile


class UserLoginView(LoginView):
    # 指定一个用于接收到 GET 请求时，需要返回的模板文件
    template_name = 'users/login.html'

  
class UserLogoutView(LogoutView):
    # 用户退出登录后，将要跳转的 URL
    # next_page = "/"
    next_page = reverse_lazy('users:login')

class UserRegisterFormView(FormView):
    template_name= 'users/register.html'
    form_class = UserRegisterModelForm
    success_url = reverse_lazy('users:login')
    def form_valid(self,form):
        user = UsersProfile(**form.cleaned_data)
        user.set_password(form.cleaned_data['password'])
        user.save()

        return super().form_valid(form)
    def form_invalid(self, form):
          # 数据无效返回原来的模板，并且携带原来提交的数据
        print("form-->", form)
        return super().form_invalid(form)
