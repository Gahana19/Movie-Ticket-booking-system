from unicodedata import name
from django.contrib import admin
from django.urls import path, include



from . views import (
    signup_views,
    login_view,
    forget_password_view,
    reset_password_view,
    logout_view
)
urlpatterns = [
    path('signup/', signup_views.as_view(), name='signup'),
    path('login/', login_view.as_view(), name='login'),
   
    path('forget/', forget_password_view, name='forget'),
    path('reset/', reset_password_view, name='reset'),
    path('logout/', logout_view, name='logout'),



]
