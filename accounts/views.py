from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        #Getting Form Values

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #Checking Password

        if password == password2:
                if User.objects.filter(username=username).exists():
                        messages.error(request,'Username Already Taken') 
                        return redirect('register')
                else :
                        if User.objects.filter(email=email).exists():
                                messages.error(request,'Email Already Taken') 
                                return redirect('register')
                        else:
                                user = User.objects.create_user(username=username,password=password,email=email,
                                first_name=first_name,last_name=last_name)
                                #login after Register
                                # auth.login(request,user)
                                # messages.success(request,'You are Now Logged in')
                                # return redirect('/index')
                                user.save();
                                messages.success(request,'You are Now Registered and can Login')
                                return redirect('login')



        else:
            messages.error(request,'Passwords do not Match')
            return redirect()    

    else:
     return render(request,'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
                auth.login(request,user)
                messages.success(request,'You are Now Logged In')
                return redirect('dashboard')
        else:
                messages.error(request,'Invalid Credentials')
                return redirect('login')
    else:
     return render(request,'accounts/login.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request,'accounts/dashboard.html')
