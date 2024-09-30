from django.shortcuts import render,redirect
from app.forms import RegisterationForm,LoginForm,TodoCreateForm

# ,TodolistForm,TodocalenderForm
from django.views.generic import View
from django.contrib import messages
from app.models import todolist


from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import login,logout,authenticate
from django.utils.decorators import method_decorator

from app.decorators import signin_required 
# Create your views here.

class SignupView(View):

    def get(self,request,*args,**kwargs):

        form_instance=RegisterationForm()

        return render(request,"registration.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance = RegisterationForm(request.POST)



        if form_instance.is_valid():

            form_instance.save()

            messages.success(request,"Registration Complete")

            return redirect("login")
        
        else:

            messages.error(request,"Registration failed")

            return render(request,"registration.html",{"form":form_instance})
        
class LoginView(View):
    def get(self,request,*args,**kwargs):

        form_instance = LoginForm()

        return render(request,"login.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=LoginForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            user_obj=authenticate(request,**data)

            if user_obj:

                login(request,user_obj)
                messages.success(request,"Login Successfull")

                return redirect("todo-list")
            
        else:
            messages.error(request,"Login Failed")
            return render(request,"login.html",{"form":form_instance})
        

@method_decorator(signin_required,name="dispatch")        
class LogoutView(View):

    def get(self,request,*args,**kwargs):

        logout(request)

        messages.success(request,"Logout Successfully")
        return redirect("login")

@method_decorator(signin_required,name="dispatch")
class TodoCreateView(View):
    def get(self,request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"invalid session...Please login")
            return redirect("login")
        form_instance = TodoCreateForm()

        return render(request,"todocreate.html",{"form":form_instance})
    def post(self,request,*args,**kwargs):

        form_instance = TodoCreateForm(request.POST)

        if form_instance.is_valid():

            form_instance.instance.owner=request.user

            form_instance.save()
           
            messages.success(request,"Task added successfully")

            return redirect("todo-list")
        
        else:

            return render(request,"todolistcreate.html",{"form":form_instance})
        

@method_decorator(signin_required,name="dispatch")       
class TodolistView(View):
    def get(self,request,*args,**kwargs):
        
        qs = todolist.objects.filter(owner=request.user).order_by('-id')

           

        return render(request,"todolist.html",{"table":qs})
    


@method_decorator(signin_required,name="dispatch")    
class TodoupdateView(UpdateView):
    model = todolist
    form_class = TodoCreateForm

    template_name= "todoupdate.html"
    
    success_url = reverse_lazy("todo-list")

@method_decorator(signin_required,name="dispatch")
class TodocompleteView(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        qs = todolist.objects.filter(id=id)
        qs.update(status = "Completed")
        messages.success(request,"Task completed Successfully..! CONGRATULATION")
        return redirect("todo-list")
    

@method_decorator(signin_required,name="dispatch")    
class TodoDeleteView(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        todolist.objects.get(id=id).delete()
        messages.success(request,"Task removed succesfully")
        return redirect("todo-list")
    



@method_decorator(signin_required,name="dispatch")          
class Todopersonalview(View):
    def get(self,request,*args,**kwargs):
        qs = todolist.objects.filter(type = "personal",owner = request.user)
        return render(request,"todopersonal.html",{"table":qs})


@method_decorator(signin_required,name="dispatch")  
class Todoworkview(View):
    def get(self,request,*args,**kwargs):
        qs = todolist.objects.filter(type = "work",owner = request.user)
        return render(request,"todowork.html",{"table":qs})
@method_decorator(signin_required,name="dispatch")  
class Todowishlistview(View):
    def get(self,request,*args,**kwargs):
        qs = todolist.objects.filter(type = "wishlist",owner = request.user)
        return render(request,"todowishlist.html",{"table":qs})

@method_decorator(signin_required,name="dispatch")  
class Todoshoppingview(View):
    def get(self,request,*args,**kwargs):
        qs = todolist.objects.filter(type = "Shopping",owner = request.user)
        return render(request,"todoshopping.html",{"table":qs})
    
# class FilterbyDateView(View):
#     def get(self,request,*args,**kwargs):
#         form_instance = FilterdateForm()
#         return render(request,"filterbydate.html",{"form":form_instance})
#     def post(self,request,*args,**kwargs):
#         form_instance = FilterdateForm(request.POST)
        
#         print(data)
#         date = form_instance.value
#         qs = todolist.objects.filter(due_date = date)
#         return render(request,"filterbydate.html",{"form":form_instance,"table":qs})
        
        
    






