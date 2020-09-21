from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from theblog.models import UserProfile

from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm

# Create user
class UserRegisterView(generic.CreateView):
  form_class    = SignUpForm
  template_name = 'registration/register.html'
  success_url   = reverse_lazy('login')

# Create profile page
class CreateProfilePageView(CreateView):
  model         = UserProfile
  form_class    = ProfilePageForm
  template_name = 'registration/create_user_profile_page.html'
  # fields        = '__all__'
  # success_url   = reverse_lazy('home')
  # function to get userid of loggendin user and use it to save profilepage
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

# Show profile page
class ShowProfilePageView(DetailView):
  model         = UserProfile
  template_name = 'registration/show_user_profile.html'
  # function to make data usable in html
  def get_context_data(self, *args, **kwargs):
    # users = UserProfile.objects.all()
    context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
    page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])
    context["page_user"] = page_user
    return context

# Edit profile page
class EditProfilePageView(generic.UpdateView):
  model         = UserProfile
  template_name = 'registration/edit_profile_page.html'
  fields        = ['bio', 'profile_pic', 'website_url', 'twitter_url', 'facebook_url']
  success_url   = reverse_lazy ('home')

# Edit user
class UserEditView(generic.UpdateView):
  form_class    = EditProfileForm
  template_name = 'registration/edit_settings_page.html'
  success_url   = reverse_lazy('home')

  def get_object(self):
    return self.request.user

# Change password (class-based view)
class PasswordChangingView(PasswordChangeView):
  # form_class  = PasswordChangeForm
  form_class  = PasswordChangingForm
  # success_url = reverse_lazy('home')
  success_url = reverse_lazy('password_success')
  
# password success (functional view)
def password_success(request):
  return render(request, 'registration/password_success.html', {})

