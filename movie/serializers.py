from rest_framework.serializers import ModelSerializer

from .models import Movie, Review


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieSerializer(ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
