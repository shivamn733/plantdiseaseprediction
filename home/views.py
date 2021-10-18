from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse ,redirect
from home.models import contact, profile 
from datetime import datetime
import json
from django import forms
import uuid
from .models import *
from django.contrib import messages
import requests 
from django.conf import settings
from django.core.mail import send_mail
from .forms import UploadFileForm

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
import PIL.Image
import numpy as np
import os
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import json
from keras.models import load_model
# Create your views here.
model =load_model("model/pridict-model.h5")


def handle_uploaded_file(f):
    with open('media/img2.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
def index(request):
    #print("fffff")
    if request.user.is_anonymous:
        print("fffff")
        return redirect("/ulogin")
    '''if request.method=='POST':
        name=request.POST['name']
        phone=request.POST.get('phone')
        im=request.FILES['fileu']
        
        print(im)
        cont=contact(name=name,phone=phone,date=datetime.today(),im=im)
        cont.save()'''
    return render(request,'index.html')
    #return HttpResponse("this is b")
def ulogin(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        print(username,password)
        clientkey=request.POST.get("g-recaptcha-response")
        #print(clientkey)
        secretkey="6LerMVQbAAAAAJIPNRQ_LogvoskfDgFKgLh4G7tY"
        captchadata={
            'secret': secretkey, 
           'response': clientkey
        }
        
        r=requests.post('https://www.google.com/recaptcha/api/siteverify',data=captchadata)
       
        response=json.loads(r.text)
        verify=response.get('success')
        print("response is given ::",verify)
        if verify==0:
            print("verify is false")
            return redirect("/")

        user = authenticate(username=username,password=password)
        if user is not None:
            print("user vferi")
            login(request,user)
            print("login kr rha")
            return redirect("/")
        # A backend authenticated the credentials
        else:
            print("w pass")
        # No backend authenticated the credentials
            return render(request,'ulogin.html')

        #checking if user is logged in 
    return render(request,'ulogin.html')
def ulogout(request):
    logout(request)
    return redirect("/ulogin")
def reg(request):
    if request.method =="POST":
        name=request.POST.get('name')
        um=request.POST.get('username')
        passw=request.POST.get('password')
        email=request.POST.get('email')
        print(passw)
        if User.objects.filter(username=um).first():
            messages.success(request, 'Username is taken')
            return redirect('/reg')
        if User.objects.filter(email=email).first():
            messages.success(request, 'email is taken')
            return redirect('/reg')
        
        cont=User(first_name=name,username=um,email=email)
        cont.set_password(passw)
        authtoken=str(uuid.uuid4())
        prof=profile(user=cont,auth_token=authtoken)
        mail_after_reg(authtoken,email)

        
        cont.save()
        prof.save()
        return redirect("/tokens")
    return render(request,"reg.html")
def suc(request):
    return render(request,"suc.html")
def tokens(request):
    return render(request,"token_send.html")
def mail_after_reg(token,mail):
    subject="mail for profile verification"
    massage=f"paste it for verification http://127.0.0.1:8000/verify/{token}"
    email_from=settings.EMAIL_HOST_USER
    recepient=[mail]
    send_mail(subject,massage,email_from,recepient)
def verify(request,authtoken):
    profile_o=profile.objects.filter(auth_token=authtoken).first()
    if profile_o:
        profile_o.is_verify=True
        profile_o.save()
        messages.success(request, 'email verified')
        return redirect("/ulogin")
def upl(request):
    
    if request.method == 'POST':
        print("ifff part")
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print("validddd")
            handle_uploaded_file(request.FILES['fileu'])
        #return HttpResponseRedirect('/success/url/')
        ########flask ffff
            c=pred_cot_disease()

    else:
        print("else part")
        form = UploadFileForm()
    print(c)
    
    if(c==0):
        context ={
        "var":"Disease NO 0",
        "var2":"this is var 2"
    }
    if(c==1):
        context ={
        "var":"Disease NO 1",
        "var2":"this is var 2"
    }
    if(c==2):
        context ={
        "var":"Disease NO 2",
        "var2":"this is var 2"
    }
    if(c==3):
        context ={
        "var":"Disease NO 3",
        "var2":"this is var 2"
    }
    if(c==4):
        context ={
        "var":"Disease NO 4",
        "var2":"this is var 2"
    }
    if(c==5):
        context ={
        "var":"Disease NO 5",
        "var2":"this is var 2"
    }
    if(c==6):
        context ={
        "var":"Disease NO 6",
        "var2":"this is var 2"
    }
    if(c==7):
        context ={
        "var":"Disease NO 7",
        "var2":"this is var 2"
    }
    if(c==8):
        context ={
        "var":"Disease NO 8",
        "var2":"this is var 2"
    }
    if(c==9):
        context ={
        "var":"Disease NO 9",
        "var2":"this is var 2"
    }
    return render(request, 'r9.html',context)
def pred_cot_disease():
  test_image = load_img("media/img2.jpg", target_size = (150, 150)) # load image 
  print("@@ Got Image for prediction")
   
  test_image = img_to_array(test_image)/255 # convert image to np array and normalize
  #print(test_image)
  test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
   
  result = model.predict(test_image).round(3) # predict diseased palnt or not
  #result=[0,1,3,4,6,7]
  print('@@ pred....')
  print('@@ Raw result = ', result)
  print('@@ pred....')
   
  pred = np.argmax(result) # get the index of max value
  print(pred)
  if pred==2:
    print("in2")
  return pred
 





