from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import datetime
from . import models



def about_us(request):
    return render(request, "about.html")



def date_now(request):
   a = datetime.datetime.now()
   return render(request, 'date_now.html', {'dat': a})


def film_show(request):
    shows = models.Film.objects.all()
    return render(request, "films_show.html", {"shows":shows})

def films(request , id):
    # film = models.Film.objects.all()
    film = get_object_or_404(models.Film, id=id)
    return render(request, "films.html", {"film":film})


def rewiev(request , id):
    rewiev = get_object_or_404(models.Rewiev.objects.filter(id_pole=id))
    return render(request, "rewievs_film.html",{"rewiev":rewiev})
