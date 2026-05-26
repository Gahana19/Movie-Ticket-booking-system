from django.db import models
from django.utils import timezone
from datetime import datetime



# Create your models here.
class Movie(models.Model):
    LANGUAGE_CHOICES=[
         ('Hindi','Hindi'),
        ('Nepali','Nepali'),
        ('English','English'),
        ]

    movie_id= models.CharField(max_length=10,null=True)
    movie_name = models.CharField(max_length=100)
    image=models.ImageField(upload_to='image/', null=True,  blank=True)
    genre = models.CharField(max_length=50)
    language = models.CharField(max_length=15,choices= LANGUAGE_CHOICES)
    duration=models.CharField(max_length=100)
    release_date = models.DateField()   
    showtimes = models.TimeField()
    ticket_price = models.DecimalField(max_digits=6, decimal_places=2, default=100.0)

    created_at = models.DateTimeField(auto_now=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self): 
        return self.movie_name

    
    



