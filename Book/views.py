from django.shortcuts import render, redirect
from .models import Booking
from django.http import HttpRequest
from django.urls import reverse



def book_ticket(request: HttpRequest):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        movie = request.POST['movie']
        date = request.POST['date']
        time = request.POST['time']
        seats = request.POST['seats']
        price_per_ticket = int(request.POST['price_per_ticket'])
        total_price = int(request.POST['total_price'])

        booking = Booking.objects.create(
            name=name,
            email=email,
            movie=movie,
            date=date,
            time=time,
            seats=seats,
            price_per_ticket=price_per_ticket,
            total_price=total_price
        )

        return redirect(f"{reverse('booking_summary')}?id={booking.id}")


    
    return render(request, 'book/ticket.html')

def booking_summary(request):
    booking_id = request.GET.get('id')
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'book/bill.html', {'booking': booking})
