from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import datetime
from . import models, forms
from .forms import PostForm
from django.shortcuts import redirect


def about_us(request):
    return render(request, "about.html")



def date_now(request):
   a = datetime.datetime.now()
   return render(request, 'date_now.html', {'dat': a})



def film_show(request):
    film = models.Film.objects.all()
    return render(request, "all_films.html", {"film": film})


def film_detail(request, id):
    show =get_object_or_404(models.Film, id=id)
    return render(request, "films_detail.html", {"film":show})



def films(request , id):
    # film = models.Film.objects.all()
    film = get_object_or_404(models.Film, id=id)
    return render(request, "films.html", {"film":film})



def rewiev(request , id):
    rewiev = get_object_or_404(models.Rewiev.objects.filter(id_pole=id))
    return render(request, "rewievs_film.html",{"rewiev":rewiev})




def add_film(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponse("Фильм успешно добавлен")
    else:
        form = PostForm()
    return render(request, "add_film.html", {'form': form})


# def comment(request):
#     comment = models.FilmComment.objects.all()
#     return render(request, "films_detail.html", {"comment": comment})

