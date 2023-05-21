from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from .models import TodoModel
from .forms import TodoForm,Loginform,RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
# Create your views here.

def sign_required(fun):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fun(request,*args,**kwargs)
        else:
            messages.warning(request,"login required for this action")
            return redirect("signin")
    return inner

@method_decorator(sign_required,name='dispatch')
class Home(View):
    def get(self,request,*args,**kwargs):
        form=TodoForm()
        data=TodoModel.objects.all()
        return render(request,"home.html",{'todoform':form,'tododata':data})
    def post(self,request,*args,**kwargs):
        todo_data=TodoForm(data=request.POST)
        if todo_data.is_valid():
            todo_data.save()
            messages.success(request,"new todo is added")
            return redirect('home')

class DelTodo(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        TodoModel.objects.filter(id=id).delete()
        return redirect('home')
class SignIn(View):
    def get(self,request,*args,**kwargs):
        form=Loginform()
        return render(request,'signin.html',{'form':form})
    def post(self,request,*args,**kwargs):
        signin_data=Loginform(data=request.POST)
        if signin_data.is_valid():
            uname=signin_data.cleaned_data.get('username')
            pswd=signin_data.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=pswd)
            if user:
                login(request,user)
                messages.success(request,'login success')
                return redirect('home')
            else:
                messages.success(request,'login failed')
                return render(request,'signin.html',{'form',signin_data})
            
class SignUp(View):
    def get(self,request,*args,**kwargs):
        form=RegisterForm()
        return render(request,'signup.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form=RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registration successful')
            return redirect('signin')
        else:
            messages.success(request,'Registration failed')
            return render(request,'signup.html',{'form',form})

@method_decorator(sign_required,name='dispatch')
class LgOut(View):
    def get(selg,request,*args,**kwargs):
        logout(request)
        return redirect("signin")