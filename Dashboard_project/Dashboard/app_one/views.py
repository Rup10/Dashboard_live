from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
def HomePage(request):
    return render (request, 'home.html')

def LoginPage(request):
    return render (request, 'login.html')

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass1 = request.POST.get('password2')
        new_user = User.objects.create_user(uname, email, pass1)
        new_user.save()
        return redirect('login')
        # print(uname)

    return render (request, 'signup.html')