from django.urls import path, include
from . import views

urlpatterns = [

    path('films/<int:id>/',views.films),
    path('rewiev/<int:id>/',views.rewiev),


]
