from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_ticket, name='book_ticket'),
    path('bill/', views.booking_summary, name='booking_summary'),

    
]
