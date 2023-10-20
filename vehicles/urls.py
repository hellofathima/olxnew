from django.contrib import admin
from django.urls import path
from vehicles.views import SignUpView,SignInView,AutoCreateView,AutoListView,IndexView,AutoDetailView,AutoUpdateView,remove_autos
urlpatterns = [
    
path("signup",SignUpView.as_view(),name="signup"),
path("signin",SignInView.as_view(),name="signin"),
path("autoadd/",AutoCreateView.as_view(),name="auto-add"),
path("autos/all",AutoListView.as_view(),name="auto-list"),
path("autos/<int:pk>/remove",remove_autos,name="remove-autos"),
path("autos/<int:pk>/change/",AutoUpdateView.as_view(),name="change-autos"),
path("autos/<int:pk>/",AutoDetailView.as_view(),name="auto-detail"),
path("index",IndexView.as_view(),name="index"),

]
