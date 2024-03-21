import requests
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
import string
import random

from . import forms
from . forms import IntegerDateForm, PieChartForm


# Create your views here.
def hello(request):
    return render(request,'hello123.html')
def hello1(request):
    return HttpResponse("<center><font color=blue>Welcome to TTM Homepage</center>")

def Newhomepage(request):
    return render(request,'Newhomepage.html')
def travelpackage(request):
    return render(request,'travelpackage.html')
def print1(request):
    return render(request,'print_to_console.html')
def print_to_console(request):
    if request.method == "POST":
        User_Input= request.POST['User_Input']
        print(f'User_Input:{User_Input}')
    #return HttpResponse('Form Submitted Successfully')
    a1={'User_Input':User_Input}
    return render(request,'print_to_console.html',a1)
def random123(request):
    ran1 = ''.join(random.sample(string.digits, k=6))
    print(ran1)
    a2={"ran1":ran1}
    return render(request,'random123.html',a2)
def ran(request):
    return render(request,"Randomotp.html")

def randomotp(request):
    if request.method == "POST":
        Input1= request.POST['Input1']
        input2=int(Input1)
        result_str=''.join(random.sample(string.digits,input2))
        print(result_str)
        context={'result_str':result_str}
    return render(request,"Randomotp.html",context)
def getdate1(request):
    return render(request,'get_date.html')
import datetime
from django.shortcuts import render
def get_date(request):
    if request.method=='POST':
        form=IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value=form.cleaned_data['integer_value']
            date_value=form.cleaned_data['date_value']
            updated_date=date_value + datetime.timedelta(days=integer_value)
            return render(request,'get_date.html',{'updated_date':updated_date})
        else:
            form=IntegerDateForm()
        return render(request,'get_date.html',{'form':form})

def tzfunctioncall(request):
    return render(request,'pytzexample.html')
def data(request):
    return render(request,'Register.html')
from . models import *
def registerloginfunction(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phonenumber=request.POST.get('phonenumber')
        if Register.objects.filter(email=email).exists():
            message1="Email already registered. Choose a different email."
            return render(request,'Register.html',{'message1':message1})
        Register.objects.create(name=name,email=email,password=password,phonenumber=phonenumber)
        return redirect('Newhomepage')
    return render(request,'Register.html')
import matplotlib.pyplot as plt
import numpy as np

def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1={'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'Pie_Chart.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'Pie_Chart.html', {'form': form})
def Photos(request):
    return render(request,"Photos.html")
def weathercall(request):
    return render(request,'weatherappinput.html')
def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '7e0c764b535e5ed445fedcf32e0d8eb4'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1= round(temperature - 273.15,2)
            return render(request, 'weatherappinput.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherappinput.html', {'error_message': error_message})
def login(request):
    return render(request,'login.html')
def sinup(request):
    return render(request,'sinup.html')
def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return render(request,"Newhomepage.html")
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')
def sinup1(request):
    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['password']
        pass2=request.POST['password1']
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'OOPS! Username already taken')
                return render(request,'sinup.html')
            else:
                user=User.objects.create_user(username=username,password=pass1)
                user.save()
                messages.info(request,'Account created successfully')
                return render(request,'login.html')
        else:
            messages.info(request,'Password do not match')
            return render(request,'sinup.html')
def logout(request):
    auth.logout(request)
    return render(request,'Newhomepage.html')
# def contactmail1(request):
#     return render(request,'contact.html')
# def contactmail(request):
#     if request.method=="POST":
#         firstname=request.POST['firstname']
#         lastname=request.POST['lastname']
#         email=request.POST['email']
#         comments=request.POST['comment']
#         tosend=comments +'-------------------------------------This is just the'
#         data=contactus(firstname=firstname,lastname=lastname,email=email,comments=comments)
#         data.save()
#         return HttpResponse("<h1><center>Thank you for giving Feedback</center></h1>")


def send_email(request):
    if request.method == 'POST':
        sender_email = request.POST.get('sender_email')
        recipient_email = request.POST.get('recipient_email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        try:
            # Send email
            send_mail(
                subject,
                message,
                sender_email,
                [recipient_email],
                fail_silently=False,
            )
            return HttpResponse('Email sent successfully!')
        except Exception as e:
            return HttpResponse('Error sending email: ' + str(e))
    else:
        return render(request, 'mail.html')



