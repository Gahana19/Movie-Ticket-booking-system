from django.contrib import admin
from django.urls import path,include


from .import views
urlpatterns = [
    path('',views.index_page, name='index'),
    
    path('main_dashboard', views.main_dashboard,
    name='main_dashboard')
]