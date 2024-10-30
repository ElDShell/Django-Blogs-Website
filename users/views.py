from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model
from django.views.generic import View,CreateView,DetailView,UpdateView,TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordResetView,PasswordResetConfirmView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import * 
from .models import *
from .utils import *
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import SetPasswordForm

# Create your views here.
class Register(CreateView):
    model = User
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    form_class= RegisterForm
    def form_valid(self, form):
        messages.success(self.request,'User Created Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'There was an error with your submission.')  # This will show you the errors in the console.
        return super().form_invalid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(self.request, 'You are already Logged in')
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

class Login(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        super().form_valid(form)
        next_url = self.request.GET.get('next',self.success_url) 
        messages.success(self.request,f'You have Successfully Logged in, Welcome {self.request.user.username}')
        return redirect(next_url)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(self.request,'You are already Logged in')
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    
class Logout(LoginRequiredMixin,LogoutView):
    template_name = None
    
    def post(self, request, *args, **kwargs):
        respone = super().post(request,*args, **kwargs)
        messages.warning(self.request,'You have Logged out')
        return respone
    
class ChagePasswrod(LoginRequiredMixin,PasswordChangeView):
    template_name= 'change_password.html'
    success_url = reverse_lazy("login")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['profile'] = self.request.user.profile
        return context
    def form_valid(self, form):
        respone = super().form_valid(form)
        messages.success(self.request,"Password Change Successfully")
        return respone
    
class ProfileDetial(LoginRequiredMixin,DetailView):
    model = Profile
    template_name = 'profile_content.html'
    def get_context_object_name(self, obj):
        return 'profile'

class ProfileUpdate(LoginRequiredMixin,UpdateView):
    model = Profile
    template_name = 'profile_update.html'
    fields = ['name','image','date_of_birth','description','fblink','instlink','twlink','lilink']
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        if self.object.user != request.user:
            return self.handle_no_permission()
        else :
            context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
    
    
    def get_success_url(self):
        profile = self.get_object()
        return reverse_lazy("profile_update",args=[profile.id])
    def form_valid(self, form):
        update_profile_message(self.request)
        return super().form_valid(form)
    
class ProfileImageUpdateView(LoginRequiredMixin,UpdateView):
    model=Profile
    form_class = ProfileImageForm
    template_name= None
    

    def get_success_url(self):
        profile = self.get_object()
        return reverse_lazy("profile_update",args=[profile.id])
    
    def get_object(self):
        return self.request.user.profile
    
    def form_valid(self, form):
        profile = self.get_object()
        
        profile.image.delete(save=False)
        profile.image = self.request.FILES.get("profile_img")
        profile.save()
        
        update_profile_message(self.request)

        return super().form_valid(form)

class ProfileImageDeleteView(LoginRequiredMixin,UpdateView):
    model = Profile
    form_class = ProfileImageForm
    template_name = None

    def get_object(self):
        return self.request.user.profile
    
    def get_success_url(self):
        profile = self.get_object()
        return reverse_lazy("profile_update",args=[profile.id])
    
    def form_valid(self, form):
        profile = self.get_object()
        
        if profile.image:
            profile.image.delete(save=False) 
            profile.image = None
            profile.save()
            update_profile_message(self.request)
        else:
            messages.warning(self.request,"There is no image to delete")
        return super().form_valid(form)

# reset password 
class ResetPasswordView(PasswordResetView):
    token_generator = ResetPasswordToken()
    html_email_template_name = 'password_reset\\password_reset_email.html'
    template_name = "password_reset\\password_reset.html" 
    success_url = reverse_lazy('password_reset_done')
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(self.request, 'You are already Logged in')
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    
class ResetPasswordDoneView(TemplateView):
    template_name= "password_reset\\password_reset_done.html"

class ResetPasswordConfirmView(PasswordResetConfirmView):
    token_generator = ResetPasswordToken()
    template_name = "password_reset/password_reset_confirm.html"
    success_url = reverse_lazy('login')

    def get_success_url(self):
        messages.success(self.request, "Your account password has been changed successfully")
        return super().get_success_url()

    def dispatch(self, request, *args, **kwargs):
        print('##################dispatch-Method######################')# test line
        uid = kwargs.get('uidb64')
        combined_token = kwargs.get('token')

        try:
            uid = urlsafe_base64_decode(uid).decode()
            user = get_user_model().objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
            user = None

        if user is not None and combined_token:
            print('dispatch Say: Entering token validation check')# test line
            is_token_valid = self.token_generator.check_token(user, combined_token)

            if is_token_valid:
                if request.method == 'POST':
                    form = SetPasswordForm(user, request.POST)
                    if form.is_valid():
                        form.save()  
                        messages.success(request, "Your password has been reset successfully.")
                        return redirect(self.get_success_url())  # Redirect to success URL
                else:
                    # If GET request, render the empty form
                    form = SetPasswordForm(user)

                # Render the form with any errors if present
                return render(request, self.template_name, {'form': form})

        messages.warning(request, "This password reset link is either invalid or has already been used.")
        return render(request, 'password_reset/already_used.html')

# Functions
def update_profile_message(request):
    messages.success(request,"Profile has been updated")

