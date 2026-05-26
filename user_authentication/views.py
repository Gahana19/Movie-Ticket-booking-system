from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string
from django.utils import timezone
from django.views.generic import FormView
from user_authentication.models import CustomUser, PasswordResetRequest
from user_authentication.form import SignupForm, LoginForm,ForgetPasswordForm, ResetPasswordForm



# Create your views here.
class AuthViewMixin:
    def handle_authenticated_user(self, request):
        if request.user.is_authenticated:
            if request.user.is_admin:
                return redirect('main_dashboard')
            elif request.user.is_client:
                return redirect('customer_dashboard')
        return None
class signup_views(AuthViewMixin, FormView):
    template_name = 'auth/signup.html'
    form_class = SignupForm

    def get(self, request, *args, **kwargs):
        redirect_response = self.handle_authenticated_user(request)
        if redirect_response:
            return redirect_response
        return super().get(request, *args, **kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, 'Signup successful!')
        return redirect('index')
        # Send welcome email
        # self.send_welcome_email(user)
#       # Redirect based on role
        # return self.redirect_by_role(user)
    # def send_welcome_email(self, user):
    #     subject = 'Welcome to Our Platform'
    #     message = f'Hi {user.first_name},\n\nThank you for registering with us!'
    #     send_mail(
    #     subject,
    #     message,
    #     settings.DEFAULT_FROM_EMAIL,
    #     [user.email],
    #     fail_silently=False,
    #)
    # def redirect_by_role(self, user):
    #     if user.is_admin:
    #         return redirect('main_dashboard')
    #     elif user.is_client:
    #         return redirect('customer_dashboard')
    #     return redirect('index')
class login_view(AuthViewMixin, FormView):
    template_name = 'auth/login.html'
    form_class = LoginForm # Use the defined form

    def get(self, request, *args, **kwargs):
        redirect_response = self.handle_authenticated_user(request)
        if redirect_response:
            return redirect_response
        return super().get(request, *args, **kwargs)
    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
            messages.success(self.request, 'Login successful!')
            return self.redirect_by_role(user)
        messages.error(self.request, 'Invalid credentials!')
        return redirect('login')
    def redirect_by_role(self, user):
        if user.is_admin:
            return redirect('main_dashboard')
        elif user.is_client:
            return redirect('customer_dashboard')
        return redirect('main_dashboard')

    

  
# method to forget password
def forget_password_view(request):
    if request.method == 'POST':
        form = ForgetPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = CustomUser.objects.get(email=email)
            
            # Delete any existing reset requests for this user
            PasswordResetRequest.objects.filter(user=user).delete()
            
            # Create new reset request
            token = get_random_string(32)
            reset_request = PasswordResetRequest.objects.create(
                user=user,
                email=email,
                token=token
            )
            # Send reset email
            reset_request.send_reset_email()
            
            messages.success(request, 'Password reset link has been sent to your email')
            return redirect('login')
    else:
        form = ForgetPasswordForm()
    
    return render(request, 'auth/forget.html', {'form': form})


def reset_password_view(request, token):
     reset_request = PasswordResetRequest.objects.filter(token=token).first()

     if not reset_request or not reset_request.is_valid():
         messages.error(request, 'Invalid or Expired reset link')
         return redirect('index')
     if request.method == 'POST':
         new_password = request.POST['new_password']
         reset_request.user.set_password(new_password)
         reset_request.user.save()
         messages.success(request, 'Password reset successful')
         return redirect('login')
     return render(request, 'auth/reset.html', {'token': token })    

     #to logout
def logout_view(request):
    logout(request)
    messages.success(request, 'logout successful')
    return redirect('index')      
         

