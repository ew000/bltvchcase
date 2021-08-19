from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class MovieApiView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    #permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        snippets = Movie.objects.all()
        serializer = MovieSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        try:
            user = self.request.user
            movie_id = self.request.data.get('movie_id' or None)
            print(movie_id)
            snippet = Movie.objects.get(id=movie_id, created_by=user)
            snippet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Movie.DoesNotExist:
            return Response({"err_code:1000"}, status=status.HTTP_400_BAD_REQUEST)


class ReviewApiView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        snippets = Review.objects.all()
        serializer = ReviewSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        try:
            user = self.request.user
            movie_id = self.request.data.get('review_id' or None)
            print(movie_id)
            snippet = Review.objects.get(id=movie_id, user=user)
            snippet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Movie.DoesNotExist:
            return Response({"err_code:1000"}, status=status.HTTP_400_BAD_REQUEST)
