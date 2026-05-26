from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns = [
    path('',views.customer_dashboard, name='customer_dashboard'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('display_movie',views.display_movie , name='display_movie'),
    path('view_movie/<int:id>',views.view_movie, name='view_movie'),
    path('delete_movie/<int:id>',views.delete_movie, name='delete_movie'),
    path('update_movie/<int:id>/', views.update_movie, name='update_movie'),
    

]



