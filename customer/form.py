
from email import message
from django import forms
from customer.models import Movie
from django.core.validators import RegexValidator
from datetime import datetime
from datetime import date
import re



class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'
        widgets={
            'movie_id':forms.NumberInput(attrs={'class':'form-control','id':'validationCustom01'}),
            'movie_name':forms.TextInput(attrs={'class': 'form-control','id':'validationCustom01'}),
            'image':forms.FileInput(attrs={'type':'file','class':'form-control','accept':'*.jpg, *.png,*.jpeg', 'id':'validationCustom03'}),
            'genre':forms.TextInput(attrs={'class':'form-control','id':'validationCustom02'}),
            'language':forms.Select(attrs={'class':'form-select','id':'validationCustom04'}),
            'duration':forms.TextInput(attrs={'class':'form-control','id':'validationCustom03'}),
            'release_date':forms.DateInput(attrs= {'type':'date','class':'form-control','id':'validationCustom04'}) ,
            'showtimes':forms.TimeInput(attrs={'type':'time','class':'form-control','id':'validationCustom05'}),
            'ticket_price':forms.NumberInput(attrs={'class':'form-control','id':'validationCustom05'}),
            }
       

    
    def clean_movie_id(self):
        movie_id = self.cleaned_data['movie_id']
        if not movie_id.isalnum():
            raise forms.ValidationError("Movie ID must be alphanumeric.")
        return movie_id

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 2 * 1024 * 1024:
                raise forms.ValidationError("Image file too large (max 2MB).")
            if not image.name.lower().endswith(('.png', '.jpg', '.jpeg')):
                raise forms.ValidationError("Only .jpg, .jpeg and .png formats are allowed.")
        return image

    def clean_genre(self):
        genre = self.cleaned_data['genre']
        allowed_genres = ['Action', 'Comedy', 'Drama', 'Thriller', 'Horror','Romantic']
        if genre not in allowed_genres:
            raise forms.ValidationError(f"Genre must be one of: {', '.join(allowed_genres)}.")
        return genre

    def clean_language(self):
        language = self.cleaned_data['language']
        allowed_languages = ['Hindi', 'Nepali', 'English']
        if language not in allowed_languages:
            raise forms.ValidationError("Language must be Hindi, Nepali, or English.")
        return language

    def clean_release_date(self):
        release_date = self.cleaned_data.get('release_date')
        if release_date < datetime.now().date():  # Convert datetime to date
            raise forms.ValidationError("Release date cannot be in the past.")
        return release_date









    def clean_duration(self):
        duration = self.cleaned_data.get('duration')

        if not duration:
            raise forms.ValidationError("Duration is required.")

        if not duration.isdigit():
            raise forms.ValidationError("Duration must be a number in hour.")

        duration_int = int(duration)

        if duration_int <= 0:
            raise forms.ValidationError("Duration must be a positive number.")

        if duration_int > 3:
            raise forms.ValidationError("Duration must not exceed  3 hours.")

        return duration