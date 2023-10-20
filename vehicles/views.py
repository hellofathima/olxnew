from django.shortcuts import render
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from vehicles.forms import RegistrationForm,LoginForm,AutoCreateForm,AutoChangeForm
from django.views.generic import View,TemplateView,FormView,ListView,DetailView,UpdateView,CreateView
from django.contrib.auth import authenticate,login,logout
from vehicles.models import Autos
from django.http import HttpResponse
from django.contrib import messages
from django.db.models.query import QuerySet
from typing import Any
from django.forms.models import BaseModelForm
from django.utils.decorators import method_decorator

# Create your views here.

def signin_required(fn):

    def wrapper(request,*args,**kwargs):
        if not  request.user.is_authenticated:
            messages.error(request,"invalid session!!")
            return redirect("signin")
        else:
             return fn(request,*args,**kwargs)
    return wrapper

class SignUpView(View):
    
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"signup.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,"registration completed successfully")
            
            return redirect("index")
        else:
            messages.error(request,"faild to create account")
            return render(request,"signup.html",{"form":form})
        
class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"signin.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"login success")
                return redirect("index")
            else:
                messages.error(request,"Invalid Username or Password")
                return render(request,"signin.html",{"form":form})
            
@method_decorator(signin_required,name="dispatch")             
class AutoCreateView(CreateView):
    template_name="vehicles/auto_add.html"
    form_class=AutoCreateForm
    context_object_name="autos"
    success_url=reverse_lazy("auto-add")

    def form_valid(self, form):
        messages.success(self.request,"vehicle added successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"vehicle adding failed")
        return super().form_invalid(form)
        
@method_decorator(signin_required,name="dispatch") 
class AutoListView(ListView):
    template_name="vehicles/auto_list.html"
    model=Autos
    context_object_name="autos"
    # def get_queryset(self):
    #     qs=Autos.objects.filter(user=self.request.user)
    #     return qs
 
@method_decorator(signin_required,name="dispatch")                    
class IndexView(CreateView,ListView):

    template_name="index.html"
    form_class=AutoCreateForm
    context_object_name="autos"
    success_url=reverse_lazy("index")
    model=Autos
  

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
    # def get_queryset(self):
    #     qs=Autos.objects.filter(user=self.request.user)
    #     return qs
@method_decorator(signin_required,name="dispatch") 
class AutoDetailView(DetailView):
    template_name="vehicles/auto_detail.html"
    context_object_name="autos"
    model=Autos

@signin_required
def remove_autos(request,*args,**kwargs):
    id=kwargs.get("pk")
    Autos.objects.filter(id=id).delete()
    messages.success(request,"Auto removed")
    return redirect("auto-list")


def SignOutView(request,*args,**kwargs):
    logout(request)
    return redirect("signin")


@method_decorator(signin_required,name="dispatch") 
class AutoUpdateView(UpdateView):
    template_name="vehicles/auto_edit.html"
    form_class=AutoChangeForm
    model=Autos
    success_url=reverse_lazy("auto-list")
    
    def form_valid(self, form):
        messages.success(self.request,"Dataupdated successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"failed to update Data")
        return super().form_invalid(form)
