from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import SignUpForm, SignInForm

# Create your views here.
def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()

    if(request.user.is_authenticated):
        user = User.objects.get(username = request.user.username)
        context = {
            'form': form,
            'user': user,
        }
        return render(request, 'home.html',context)
    else:
        context = {
            'form': form,
        }
    return render(request, 'SignUp.html',context)
    
def SignIn(request):
    if request.method == 'POST':
        # form = AuthenticationForm(request=request, data=request.POST)
        form  = SignInForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                user = User.objects.get(username = request.user.username)
                context = {
                    'form': form,
                    'user': user,
                }
                return HttpResponseRedirect('/')
                # return render(request, 'home.html',context)
            else:
                return redirect('login')            
    else:
        form = SignInForm()
    # if(request.user.is_authenticated):
    #     user = User.objects.get(username = request.user.username)
    #     context = {
    #         'form': form,
    #         'user': user,
    #     }
    # else:
    context = {
        'form': form,
    }

    return render(request, 'SignIn.html',context)

def PasswordReset(request):
    return render(request, 'PasswordReset.html')
def EmailConfirmation(request):
    return render(request, 'EmailConfirmation.html')
def Done(request):
    return render(request, 'done.html')
def ConfirmPassword(request):
    return render(request, 'ConfirmPassword.html')
def HomeView(request):
    return render(request, 'home.html')
def Logout(request):
    logout(request)
    return redirect('signin')