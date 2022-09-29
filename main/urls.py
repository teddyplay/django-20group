from django.urls import path, include
from . import views

urlpatterns = [


    path('films/', views.films),
    path('film_show/', views.film_show),
    path('film_show/<int:id>/', views.film_detail),
    path('films/<int:id>/',views.films),
    path('rewiev/<int:id>/',views.rewiev),
    path('add_film/', views.add_film),

]
