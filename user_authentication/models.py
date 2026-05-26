from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.conf import settings
import uuid
from django.utils.crypto import get_random_string
from django.utils import timezone

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        CLIENT = 'client','Client'
        ADMIN = 'admin','Admin'
   


    username = models.CharField(max_length=100, unique=True)

    email = models.EmailField(unique=True,db_index=True)
   
    
    first_name= models.CharField(max_length=32, blank=True)
    last_name =models.CharField(max_length=32, blank=True)

    role = models.CharField(max_length=10, choices=Role.choices, default=Role.CLIENT)
   

   #Fields for user roless
    is_admin = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    # Authentication tracking
    is_authenticated = models.BooleanField(default=False)
    login_token = models.CharField(max_length=12, blank=True, null=True)
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ['-date_joined']


   #set related_name to None to prevent reverse relation creation
    def save(self, *args, **kwargs):
        #Set username to email if not set
        if not self.username:
            self.username=self.email
        # Set role flags based on role field
        self.is_admin = (self.role == 'admin')
        self.is_client = (self.role == 'client')
        

        super().save(*args, **kwargs)



    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

 


    #groups = models.ManyToManyField(
      #  'auth.Group',
       # related_name=None,
      #  blank=True,
      #  )
    #user_permissions = models.ManyToManyField(
       # 'auth.Permission',
        #related_name=None,
        #blank=True,
        #)
        
    #def _str_(self):
        #return self.username

class PasswordResetRequest(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    email = models.EmailField()
    token = models.CharField(max_length=32, unique=True, default=get_random_string(32), editable=False)
    created_at = models.DateTimeField(auto_now_add=True)


 #define token expiration time (eg. 1 hour)
    TOKEN_VALIDITY_PERIOD = timezone.timedelta(hours=1)


    def is_valid(self):
        return timezone.now() <= self.created_at + self.TOKEN_VALIDITY_PERIOD

    def send_reset_email(self) :
        reset_link = f"http://localhost:8000/reset_password/{self.token}/ "
        send_mail(
         'Password Reset Request',
         f'Click the link to reset your password: {reset_link}',
         settings.DEFAULT_FROM_EMAIL,
         [self.email],
         fail_silently=False,
        )
 
      

