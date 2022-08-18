from django.urls import path
from .views import create_ad_view
from .api_views import AdvertisementView, HomeAdvertisementView, AdvertisementDetailView


urlpatterns = [
    path('create/', create_ad_view, name='create_ad'),
    # my urls
    path('ads/', AdvertisementView.as_view()),
    path('ads/<int:pk>', AdvertisementDetailView.as_view()),
    path('ads/home/', HomeAdvertisementView.as_view()),
]
