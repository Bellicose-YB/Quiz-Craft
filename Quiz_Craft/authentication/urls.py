from django.urls import path, include
from .views import SignUp,SignIn,PasswordReset,EmailConfirmation,Done,ConfirmPassword,Logout,HomeView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', HomeView, name='home'),
    path('signup', SignUp, name='signup'),
    path('signin', SignIn, name='signin'),
    path('passwordresetemailconfirm', auth_views.PasswordResetView.as_view(template_name='emailconfirmation.html'), name = 'passwordresetemailconfirm'),
    path('passwordresetemailconfirm/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name= 'password_reset_done'),

###### Isme doubt hai
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset_password.html'), name='password_reset_confirm'),
######


#### yeh change replace karna hai
    path('passwordreset', PasswordReset, name='passwordreset'),
    path('emailconfirmation', EmailConfirmation, name='emailconfirmation'),
    path('done', Done, name='done'),
    path('confirmpassword', ConfirmPassword, name='confirmpassword'),
    path('logout', Logout, name='logout'),
####
] 



'''
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from .views import HomeView, LoginView, LogoutView, ActivateAccountView

urlpatterns = [
    path('', HomeView, name='home'),
    path('login/', LoginView, name='login'),
    path('logout/', LogoutView, name='logout'),
    path('activate/<uidb64>/<token>/',ActivateAccountView, name='activate'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='forget_password_email.html'), name = 'password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name= 'password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset_password.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
'''