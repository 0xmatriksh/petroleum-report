from django.urls import path
from . import views

urlpatterns = [
    path('report/',views.getdata),
    path('',views.home)
]