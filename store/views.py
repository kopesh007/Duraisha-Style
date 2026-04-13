from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
import logging
from .import form
import os
from dotenv import load_dotenv
load_dotenv()
from store.models import posts 
import smtplib




def home(request):
    p1=posts.objects.get(id=1)
    p2=get_object_or_404(posts, id=2)
    p3=get_object_or_404(posts, id=3)

    return render(request,"home.html",{"p1":p1,"p2":p2,"p3":p3})
    
# Create your views here.
def product(request):
    ob=posts.objects.exclude(name__in=["about1","about2"])
    return render(request,"product.html",{"name":ob})

def detail(request,detail):
    post=posts.objects.get(name=detail)
    if detail==post.name:
        return render(request,"product_detail.html",{"data":post})
    msg="Sorry Not Found"
    return render(request,"product_detail.html",{"msg":msg})

def about(request):
    p1=posts.objects.filter(image="products/about1.jpeg").first()
    p2=posts.objects.filter(image="products/about2.jpeg").first()
    return render(request,"about.html",{"p1":p1,"p2":p2})

def con(request,price=""):
    if request.method=="POST":
        data=form.ContactForm(request.POST)
        name=request.POST.get("name")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        mess=request.POST.get("mess")
        if data.is_valid():

            msg="Data Has Been Submitted,Our Team Will Reach You"
            try:
                mail(data.cleaned_data["email"], data.cleaned_data["name"])
            except Exception as e:
                print(f"EMAIL ERROR: {e}") # This will show up in your Render Logs!

            
            return render(request,"contact.html",{"msg":msg})
        else:
            print("THAPPEYYYYYYYYY")
            return render(request,"contact.html",{"data":data,"name":name,"email":email,"subject":subject,"message":mess})
    if len(price)!=0:

        return render(request,"contact.html",{'subject':price})

    return render(request,"contact.html")
    
def mail(email,name):

    message = f"""Subject: From DURAISHA Style

Dear {name},

Thank you for your interest in DURAISHA Style.

We truly appreciate your time and effort in reaching out to us. Our team is currently reviewing your request, and we will get back to you shortly with more details.

If you have any further questions, feel free to reply to this email.

Best regards,  
DURAISHA Style  
Team Support
"""
    passward=os.getenv("email")
                                        
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("kolearning25@gmail.com",passward)
    server.sendmail("kolearning25@gmail.com",email,message)
    server.quit()

