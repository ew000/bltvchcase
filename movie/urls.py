from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60 * 3)(MovieApiView.as_view())),
    path('review/', cache_page(60 * 3)(ReviewApiView.as_view())),
]
