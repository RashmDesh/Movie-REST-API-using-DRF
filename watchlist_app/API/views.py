from watchlist_app.models import Movie
from watchlist_app.API.serializers import MovieSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

#CLASS BASED VIEW
class MovieListAV(APIView):

    def get(self,request):
        movies=Movie.objects.all()
        serializer=MovieSerializers(movies,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer=MovieSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class MovieDetailsAV(APIView):
    def get(self,request,pk):
        try:
            movie=Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'Error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)

        serializer=MovieSerializers(movie)
        return Response(serializer.data)

    def put(self,request,pk):
        movie=Movie.objects.get(pk=pk)
        serializer=MovieSerializers(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self,request,pk):
        movie=Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)















## FUNCTION BASED api VIEW
'''
@api_view(['GET','POST'])
def movie_list(request):
    if request.method=='GET':
        movies=Movie.objects.all()
        serializer=MovieSerializers(movies,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method =='POST':
        serializer=MovieSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET','PUT','DELETE'])
def movie_details(request,pk):

    if request.method=='GET':
        try:
            movie=Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'Error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)

        serializer=MovieSerializers(movie)
        return Response(serializer.data)
    
    if request.method=='PUT':
        movie=Movie.objects.get(pk=pk)
        serializer=MovieSerializers(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    if request.method=='DELETE':
        movie=Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''