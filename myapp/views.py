from django.shortcuts import render
from .models import Doctor
from random import randint
from django.core.mail import send_mail
from django.conf import settings

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
                 doctor.is_active = False
                 doctor.save()
                 message = f"Hello {fname} ,Your otp for Doctor Finder account is \n {otp}"
                 send_mail(
                 "Welcome to Doctor Finder - Verify Your Email",
                  message,
                  settings.EMAIL_HOST_USER,
                 [email],
                 fail_silently = False
                 )
                 return render(request,'otpverify.html',{'email':email})

            else:
                msg = "Password and Confirm password does not match !"
                return render(request,'register.html',{'msg':msg})

def OtpVerify(request):
    return render(request,'otpverify.html')

def OtpVerifyCheck(request):
    
        email = request.POST.get("email")
        otp = int(request.POST.get("otp"))
        user = Doctor.objects.get(email=email)
        
        if(user):
            if user.otp == otp:
                user.is_active = True
                user.save()
                msg = "Doctor successfully registered!"
                return render(request,'login.html',{'msg':msg})
            else:
                msg = "Wrong otp!"
                return render(request,'otpverify.html',{'msg':msg})
        else:
            return render(request,'register.html')
    

def Login(request):
    return render(request,'login.html')
           
def LoginValidate(request):
    if( request.method == "POST"):
        email =  request.POST.get("email")
        password =  request.POST.get("password")
        user = Doctor.objects.get(email=email)
        if(user.is_active ==True):
          if(user):
            if(user.password == password):
               return render(request,'profile.html',{'user':user})
            else:
                msg = "password does not match!"
                return render(request,'login.html',{'msg':msg})

          else:
            msg = "user with this email id does not exist! Please sign up first"
            return render(request,'register.html',{'msg':msg})

        else:
            message = "Signup before login"
            user.delete()
            return render(request,'register.html',{'msg':message})

def Hospitals(request):
    return render(request,'hospitals.html')

def Contact(request, pk):
    user = Doctor.objects.get(id=pk)
    return render(request,'contact.html',{'user':user})

def DeleteAccount(request,pk):
    user  = Doctor.objects.get(pk=pk)
    user.delete()
    return render(request,'index.html')