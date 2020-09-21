from django.urls import path
# from django.contrib.auth import views as auth_views
from . import views

from .views import UserRegisterView, UserEditView, PasswordChangingView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView

urlpatterns = [
  # create user (register)
   path('register/', UserRegisterView.as_view(), name='register'),
   # edit user
   path('edit_settings/', UserEditView.as_view(), name='edit_settings_page'),

   # edit password
   # path('password/', auth_views.PasswordChangeView.as_view(template_name= 'registration/change-password.html')),
   path('password/', PasswordChangingView.as_view(template_name= 'registration/change-password.html')),
   #  password succes url
   path('password_success', views.password_success, name='password_success'),
   # show profile page
   path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
   # edit profile page
   path('<int:pk>/edit_profile/', EditProfilePageView.as_view(), name='edit_profile_page'),
   # create profile page
   path('create_profile/', CreateProfilePageView.as_view(), name='create_profile_page'),
]