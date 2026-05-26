from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser
import re

class SignupForm(forms.ModelForm):
    confirm_password=forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'confirm_password'
        })
    )
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name', 'email','password','role']
        widgets ={
           

            'first_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter First Name',
                'minlength': '3',
                'maxlength': '50'
            }),

            'last_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter Last Name',
                'minlength': '3',
                'maxlength': '50'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@domain.com'
            }),

            'password': forms.PasswordInput(attrs={
                'type': 'password',
                'class': 'form-control',
                'placeholder': 'Password'
            }),
                

            'role': forms.Select(attrs={
                'class':'form-control',
                'placeholder':'Select Role',
            })

        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # first_name validation
        self.fields['first_name'].validators.append(
            RegexValidator(
                regex=r'^[A-Za-z\s]{3,50}$',
                message="Name should be 3-50 characters long and contain only letters and spaces."
            )
            
        ) 

        # last_name validation
        self.fields['last_name'].validators.append(
            RegexValidator(
                regex=r'^[A-Za-z\s]{3,50}$',
                message="Name should be 3-50 characters long and contain only letters and spaces."
            )
            
        )
     

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not first_name:
            raise ValidationError("First name is required.")
        if "@" in first_name:
            raise ValidationError("First name should not contain '@'")
        return first_name.strip()

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not last_name:
            raise ValidationError("Last name is required.")
        if "@" in last_name:
            raise ValidationError("Last name should not contain '@'")
        return last_name.strip()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError("Email is required.")
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            raise ValidationError("Please enter a valid email address.")
        
        # Check for duplicate email (if not editing existing instance)
        if self.instance.pk is None and CustomUser.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered.")
        return email.lower()
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise ValidationError("Password is required.")
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not any(char.isupper() for char in password):
            raise ValidationError("Password must contain at least one uppercase letter.")
        if not any(char.islower() for char in password):
            raise ValidationError("Password must contain at least one lowercase letter.")
        if not any(char.isdigit() for char in password):
            raise ValidationError("Password must contain at least one digit.")
        if not any(char in '!@#$%^&*()"_+.' for char in password):
            raise ValidationError("Password must contain at least one special character.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                raise ValidationError(
                    {'confirm_password': ValidationError("Passwords don't match", code='password_mismatch')
                })

            try:
                validate_password(password)
            except ValidationError as error:
                self.add_error('password', error)

        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.username = self.cleaned_data['email'] # Using email as username
        # Set role flags
        role = self.cleaned_data.get('role')
        user.is_client = (role == 'client')
        user.is_admin = (role == 'admin')
            
        if commit:
            user.save()
        return user
    
    
class LoginForm(forms.Form):
    email = forms.EmailField(
    widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email',
        'required': True,
        })
    )
    password = forms.CharField(
    widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'required': True,
        })
    )



"""  /*************This is for Forget password*************/  """

class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your registered email'
        })
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Email not found in our system")
        return email



""" /*************This is for Forget password*************/ """
class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'New Password'
        })
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm New Password'
        })
    )

    def clean_new_password(self):
        password = self.cleaned_data.get('new_password')
        if not password:
            raise ValidationError("Password is required.")
        
        try:
            validate_password(password)
        except ValidationError as error:
            raise ValidationError(error.messages[0])
            
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords don't match")

        return cleaned_data





