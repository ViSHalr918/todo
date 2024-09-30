from app.models import  todolist
from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

class RegisterationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-3","placeholder":"Enter your password"}),label="Password")
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-3","placeholder":"Confirm your password"}),label="Confirm Password")
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3","placeholder":"username"}))
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
        widgets = {
            
            "email":forms.TextInput(attrs={"class":"form-control mb-3","placeholder":"Enter your Email"})
        }

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3","placeholder":"Enter your username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-3","placeholder":"Enter your password"}))

class TodoCreateForm(forms.ModelForm):
    
    class Meta:
        model = todolist

        fields = ["title","due_date","type"]

        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control mb-3","placeholder":"Enter Task Here"}),
            "due_date":forms.DateTimeInput(attrs={"class":"form-control mb-3","placeholder":"Date not set","type":"date"}),
            
            
            
            

        }

# class FilterdateForm(forms.Form):
#     Date = forms.DateField(widget=forms.DateInput(attrs={"class":'form-control','type':'date'}))