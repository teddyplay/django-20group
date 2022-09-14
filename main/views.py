from django.shortcuts import render
import datetime


def about_us(request):
    return render(request, "about.html")



def date_now(request):
   a = datetime.datetime.now()
   return render(request, 'date_now.html', {'dat': a})

