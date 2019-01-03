from django.shortcuts import render,redirect
import hashlib
from .models import LoginDB
from .forms import LoginForm,SigninForm
from django.http import HttpResponse
# Create your views here.

def Encrypt(password):
    password = password.encode()
    password = hashlib.md5(password)
    password = password.hexdigest()
    return password

def login(request):
    if(request.method=='POST'):
        form = LoginForm(request.POST)
        if(form.is_valid()):
            name=request.POST['name']
            password = request.POST['password']
            password = Encrypt(password)
            
            try:
                dataname = LoginDB.objects.get(name=name)
                print(dataname.name,dataname.password)
                if(dataname.name == name and dataname.password == password):
                    context={'dataname':dataname}
                    return render(request,'live/home.html',context)
            except Exception as e:
                print(e)
                return HttpResponse("username not found")
            
    return render(request,'live/login.html')

def signin(request):
    if(request.method=='POST'):
        form = SigninForm(request.POST)
        print(form)
        if(form.is_valid()):
            password = request.POST['password']
            cpassword=request.POST['cpassword']
            if(password==cpassword):
                password = Encrypt(password)
                data = LoginDB(name=request.POST['name'],password=password)
                data.save()
                print(password)
                return redirect('login')
            else:
                return HttpResponse("please enter correct information")
        else:
            return HttpResponse("please enter correct information")
    return render(request,'live/signin.html')