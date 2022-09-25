from django.urls import path, include
from . import views

urlpatterns = [


    path('films/', views.film_show),
    path('films/<int:id>/',views.films),
    path('rewiev/<int:id>/',views.rewiev),


]
