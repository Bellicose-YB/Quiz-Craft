from django.shortcuts import render

# Create your views here.
def SignUp(request):
    return render(request, 'SignUp.html')
def SignIn(request):
    return render(request, 'SignIn.html')
def PasswordReset(request):
    return render(request, 'PasswordReset.html')
def EmailConfirmation(request):
    return render(request, 'EmailConfirmation.html')
def Done(request):
    return render(request, 'done.html')
def ConfirmPassword(request):
    return render(request, 'ConfirmPassword.html')
