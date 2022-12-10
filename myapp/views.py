from django.shortcuts import render
from .models import Doctor
from random import randint

# Create your views here.
def Index(request):
    dl = Doctor.objects.all()
    return render(request,'index.html',{'dl':dl})

def Register(request):
    return render(request,'register.html')
   



def RegistrationDoctor(request):
    if (request.method=="POST"):

        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        contact = request.POST["contact"]
        highest_degree = request.POST["highest_degree"]
        services_offers = request.POST["services_offers"]
        district = request.POST["district"]
        lat = request.POST.get("lat")
        lng = request.POST.get("lng")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")

        doctor = Doctor.objects.filter(email=email)  
        if(doctor):
            msg = "User with this email id already exist!"
            return render(request,'register.html',{'msg':msg})      
        else:
            if(password==cpassword):
                 otp = randint(100000,999999)
                 doctor = Doctor.objects.create(fname=fname,lname=lname,email=email,contact=contact,highest_degree=highest_degree,services_offers=services_offers,district=district,password=password,otp=otp,lat=lat,lng=lng)
                 return render(request,'register.html')
            else:
                msg = "Password and Confirm password does not match !"
                return render(request,'register.html',{'msg':msg})

def Login(request):
    return render(request,'login.html')
           

