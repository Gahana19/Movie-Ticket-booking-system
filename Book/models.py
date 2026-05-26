from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    movie = models.CharField(max_length=100)
    date = models.DateField()
    time = models.CharField(max_length=20)
    seats = models.CharField(max_length=200)  # comma-separated list
    price_per_ticket = models.IntegerField(default=150)
    total_price = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.movie} - {self.date}"
