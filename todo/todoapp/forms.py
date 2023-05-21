from django import forms
import re
from .models import TodoModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class TodoForm(forms.ModelForm):
    class Meta:
        model=TodoModel
        fields=['todo_desc']
        widgets={
            "todo_desc":forms.TextInput(attrs={'placeholder':'add todo','class':'form-control'}),
        }
        labels={
            "todo_desc":''
        }

class Loginform(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Username','class':'form-control'}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'placeholder':'Confirm password','class':'form-control'}))

class RegisterForm(UserCreationForm):
    password1=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'placeholder':'Enter password','class':'form-control'}))
    password2=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'placeholder':'Confirm password','class':'form-control'}))
    class Meta:
        model=User
        fields=['first_name','last_name','email','username']
        widgets={
             "first_name":forms.TextInput(attrs={'placeholder':'first_name','class':'form-control'}),
            "last_name":forms.TextInput(attrs={'placeholder':'last_name','class':'form-control'}),
            "email":forms.EmailInput(attrs={'placeholder':'email','class':'form-control'}),
            "username":forms.TextInput(attrs={'placeholder':'username','class':'form-control'}),
        }
