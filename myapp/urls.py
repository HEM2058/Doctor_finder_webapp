from django.urls import path
from myapp import views
urlpatterns = [
    path('',views.Index,name="index"),
    path('register/',views.Register,name="register"),
    path('registerdoctor/',views.RegistrationDoctor,name="registerdoctor"),
    path('otpverify/',views.OtpVerify,name="otpverify"),
    path('otpverifycheck/',views.OtpVerifyCheck,name="otpverifycheck"),
    path('login/',views.Login,name="login"),
    path('loginvalidate/',views.LoginValidate,name="loginvalidate"),
    path('hospitals/',views.Hospitals,name="hospitals"),
    path('contact/<int:pk>',views.Contact,name="contact"),
    path('deleteaccount/<int:pk>',views.DeleteAccount,name="deleteaccount")
]