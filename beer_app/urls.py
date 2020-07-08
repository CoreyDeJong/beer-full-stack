from django.urls import path
from .views import BeerList, BeerDetail

urlpatterns = [
    path('', BeerList.as_view(), name="beer_list"),
    path('<int:pk>/', BeerDetail.as_view(), name='beer_detail'),
]