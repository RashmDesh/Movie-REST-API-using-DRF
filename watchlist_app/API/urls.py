from django.contrib import admin
from django.urls import path
#from watchlist_app.API.views import movie_list,movie_details
from watchlist_app.API.views import  MovieListAV,MovieDetailsAV

urlpatterns = [
  #  path("list/",movie_list),
   # path('<int:pk>',movie_details),
    path("list/",MovieListAV.as_view()),
    path('<int:pk>',MovieDetailsAV.as_view()),
]
