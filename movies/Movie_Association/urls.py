
from django.urls import path
from .views import create_director,create_movie_table,getmovienames

urlpatterns = [
    path('director/create',create_director),
    path('moviesTable/create',create_movie_table),
    path('director/movie/<int:director_id>',getmovienames)
    
]