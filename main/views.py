from django.shortcuts import render, get_object_or_404
import datetime
from . import models



def about_us(request):
    return render(request, "about.html")



def date_now(request):
   a = datetime.datetime.now()
   return render(request, 'date_now.html', {'dat': a})


def films(request , id):
    # film = models.Film.objects.all()
    film = get_object_or_404(models.Film, id=id)
    return render(request, "films.html", {"film": film}, )
