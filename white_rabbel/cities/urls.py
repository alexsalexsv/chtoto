from django.urls import path
from .views import *


urlpatterns = [
    path('', CitiesListView.as_view(), name='home'),
    path('create/', CitiesCreateView.as_view(), name='create'),
    path('see/<int:pk>/', CitiesDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', CityUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CityDeleteView.as_view(), name='delete'),
]

