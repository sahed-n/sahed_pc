from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

# Create your views here.
def home(req):

    records = Record.objects.all()

    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']

        user = authenticate(req, username=username, password=password)

        if user is not None:
            login(req, user)
            messages.success(req, "Successfull Login for "+username+"!")
            return redirect('home')
        else:
            #messages.error(req, "There is an error!")
            messages.success(req, "There is an error!")
            return redirect('home')
    else:
        return render(req,"home.html",{'records':records})

# def login_user(req):
#     pass

def logout_user(req):
    logout(req)
    messages.success(req,"You have been logged out...")
    return redirect('home')

def register_user(req):
    if req.method == 'POST':
        form = SignUpForm(req.POST)
        if form.is_valid():
            form.save()
            #authenticate now
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # user = authenticate(req, username=username, password=password)
            user = authenticate(username=username, password=password)
            login(req,user)
            messages.success(req,"Registered Successfully! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(req,"register.html",{'form':form})
    return render(req,"register.html",{'form':form})

def customer_record(req, pk):
    if req.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(req,"record.html",{'customer_record':customer_record})
    else:
        messages.success(req,"Log in needed to view that page")
        return redirect('home')