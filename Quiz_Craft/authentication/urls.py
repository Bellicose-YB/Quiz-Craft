from django.urls import path, include
from .views import SignUp,SignIn,PasswordReset,EmailConfirmation,Done,ConfirmPassword
urlpatterns = [
    # path('', HomeView, name='home')
    path('signup', SignUp, name='signup'),
    path('signin', SignIn, name='signin'),
    path('passwordreset', PasswordReset, name='passwordreset'),
    path('emailconfirmation', EmailConfirmation, name='emailconfirmation'),
    path('done', Done, name='done'),
    path('confirmpassword', ConfirmPassword, name='confirmpassword'),
] 