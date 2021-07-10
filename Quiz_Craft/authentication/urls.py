from django.urls import path, include
from .views import SignUp,SignIn,PasswordReset,EmailConfirmation,Done,ConfirmPassword,Logout,HomeView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', HomeView, name='home'),
    path('signup', SignUp, name='signup'),
    path('signin', SignIn, name='signin'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='Emailconfirmation.html'), name = 'password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name= 'password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='PasswordReset.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='ConfirmPassword.html'), name='password_reset_complete'),
    path('logout', Logout, name='logout'),
]