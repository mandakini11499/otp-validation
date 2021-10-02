from django.shortcuts import render
from otp import settings as se
from django.core.mail import send_mail

# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def validate(request):
    uname=request.POST.get("t1")
    upwd=request.POST.get("t2")
    if uname=="maahi" and upwd=="anii":
        import random
        otp=random.randint(100000,999999)
        subject="One Time Password"
        message="Hello user this is a message from sathya tech please find your One Time Password"+str(otp)
        send_mail=(subject,message,se.EMAIL_HOST_USER,["mandakini.nimmala@gmail.com"])
        return render(request,"welcome.html",{"message":"welcome mandakini"})
    else:
        return render(request,"index.html",{"message":"Invalid User"})
