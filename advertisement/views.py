from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import AdvertisementSerializer
from ..advertisement.models import Advertisement

class AdvertisementView(APIView):
    """Advertisement API View"""

    def get(self, request):
        ads = Advertisement.objects.all()
        serializer = AdvertisementSerializer(ads, many=True)
        return Response({'ads': serializer.data})


class AdvertisementDetailView(APIView):
    """Advertisement API View"""

    def get(self, request, pk):
        ad = Advertisement.objects.get(id=self.pk)
        serializer = AdvertisementSerializer(ad)
        return Response({'ad': serializer.data})


class HomeAdvertisementView(APIView):
    """Advertisement API View for home page"""

    def get(self, request):
        ads = Advertisement.objects.all()[:10]
        serializer = AdvertisementSerializer(ads, many=True)
        return Response({'ads': serializer.data})