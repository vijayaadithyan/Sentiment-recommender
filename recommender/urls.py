from django.urls import path
from recommender.views import *
urlpatterns = [
    path('', indexpage)
]
