from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect 

def signup(request):
    if request.method == "POST" :
        if request.POST["password1"] == request.POST["password2"] :
            user = User.objects.create_user(
                username=request.POST["username"], password = request.POST["password"])
            auth.login(request,user)
            return redirect(request,'signup.html')
        else:
            return render(request,'login.html')
            

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html',{'error':'username or password is incorrect'})
    else:
        return render(request,'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'login.html')

# Create your views here.
