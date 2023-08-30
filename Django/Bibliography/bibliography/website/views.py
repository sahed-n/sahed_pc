from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record
import base64
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
def processRecords(records):
    secret_pad_left = '*>$'
    secret_pad_right = '?|`'

    for record in records:
        #encoded_data = base64.b64encode(secret_pad_left+record.id+secret_pad_right.encode()).decode()
        
        record["id"] = base64.b64encode((secret_pad_left+str(record["id"])+secret_pad_right).encode()).decode()

def decodePK(encoded_data):
    decoded_data = base64.b64decode(encoded_data).decode()
    return decoded_data


def home(req):

    #records = Record.objects.all(is_deleted=False)
    records = list(Record.objects.filter(is_deleted=False).values())
    processRecords(records)

    #return HttpResponse({"records":records})
    return JsonResponse(records, encoder=DjangoJSONEncoder, safe=False)

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
    
def delete_record(req, pk):
    if req.user.is_authenticated:
        try:
            
            ## instead of updating is_deleted in one liner, grabbing the object to check some business logics
            ## it may increase db calls

            #one thing, obejcts.get() always returns single object
            record_to_be_deleted = Record.objects.get(id=pk)

            if record_to_be_deleted.is_deleted:
                messages.success(req, "Already Deleted")
            else:
                record_to_be_deleted.is_deleted=True
                record_to_be_deleted.save()
                messages.success(req, "Record deleted")
                
        except Exception as e:
            messages.error(e)
    else:
        messages.success(req,"Action requires log in")
    
    return redirect('home')
        