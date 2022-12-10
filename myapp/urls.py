from django.urls import path
from myapp import views
urlpatterns = [
    path('',views.Index,name="index"),
    path('register/',views.Register,name="register"),
    path('registerdoctor/',views.RegistrationDoctor,name="registerdoctor"),
    path('login/',views.Login,name="login")
]