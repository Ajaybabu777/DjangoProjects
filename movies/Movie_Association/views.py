from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Director,movie_table
from rest_framework import status


@csrf_exempt
def create_director(request):
    bodyTojson = json.loads(request.body)
    directornameFromFrontend = bodyTojson['name']
    
    director = Director(name = directornameFromFrontend)
    director.save()
    
    return JsonResponse({
        "message":f'{directornameFromFrontend} Added to director table'
    })

@csrf_exempt
def create_movie_table(request):
     bodyTojson = json.loads(request.body)
     
     idOfDirector=bodyTojson["director_id"]
     
     directorId=Director.objects.get(id = idOfDirector)
     if not directorId:
         return JsonResponse ({
             "message":"director id is not in the Director table"
         })
     
     nameOfMovies=bodyTojson["movie_name"]
     
     movieList=[]
     for movieNames in nameOfMovies:
         movieList.append(movieNames)
         movie=movie_table.objects.create(movie_name = movieNames, director=directorId)
         
     return JsonResponse ({
        "message":f"{nameOfMovies} has been saved in movieTable"
    })
     
     
@csrf_exempt
def getmovienames(request, director_id):
    if request.method != "GET":
        return JsonResponse ({
            "message":"method not found"
        },status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
    else:
        movies = movie_table.objects.filter(director_id = director_id)
        movie_list = []
        for movie in movies:
            movie_list.append(movie.movie_name)
            
        return JsonResponse({
            "message":"movie name quered succesfully",
            "movies":movie_list,
            "director":director_id
            })
         