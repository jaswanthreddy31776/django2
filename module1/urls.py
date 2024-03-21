from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path("hello1", hello1),
    path("hello/",hello,name='hello'),
    path("",Newhomepage,name='Newhomepage'),
    path("card/",travelpackage,name='travelpackage'),
    path("p/",print_to_console,name='print_to_console'),
    path("print1/",print1,name="print1"),
    path('ran1/',random123,name="random123"),
    path("h1/",ran,name="ran"),
    path("context/",randomotp,name='Randomotp'),
    path("h2/",getdate1,name="getdate1"),
    path("date/",get_date,name="get_date"),
    path("py/",tzfunctioncall,name="tzfunctioncall"),
    path("data/",data,name="data"),
    path("register/",registerloginfunction,name="registerloginfunction"),
    path("chart/",pie_chart,name="Pie_Chart"),
    path("photo/",Photos,name="Photos"),
    path("w/",weathercall,name="weathercall"),
    path("wh/",weatherlogic,name="weatherlogic"),
    path("login/",login,name="login"),
    path("sinup/",sinup,name="sinup"),
    path("logout/",logout,name="logout"),
    path("sinup1/",sinup1,name="sinup1"),
    path("login1/",login1,name="login1"),
    # path("contactmail/",contactmail,name="contactmail"),
    # path("contactmail1/",contactmail1,name="contactmail1"),
    path('send_email/', send_email, name='send_email'),
]


