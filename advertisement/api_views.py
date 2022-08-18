from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import AdvertisementSerializer
from .models import Advertisement
from user.models import CustomUser


class AdvertisementView(APIView):
    """Advertisement API View"""

    def get(self, request):
        ads = Advertisement.objects.all()
        serializer = AdvertisementSerializer(ads, many=True)
        return Response({'ads': serializer.data})

    def post(self, request, *args, **kwargs):
        ad_data = request.data

        serializer = AdvertisementSerializer(data=ad_data)
        if serializer.is_valid():
            serializer.save()

        return Response({'success': f'Advertisement {ad_data["title"]} created successfully!', 'ad':serializer.data})


class AdvertisementDetailView(APIView):
    """Advertisement Details API View"""

    def get(self, request, pk):
        ad = Advertisement.objects.get(id=pk)
        serializer = AdvertisementSerializer(ad)
        return Response({'ad': serializer.data})

    def delete(self, request, pk):
        ad = Advertisement.objects.get(id=pk)
        ad.delete()

        return Response({'success': f'Advertisement deleted successfully!'})


class HomeAdvertisementView(APIView):
    """Advertisement API View for home page"""

    def get(self, request):
        ads = Advertisement.objects.all()[:10]
        serializer = AdvertisementSerializer(ads, many=True)
        return Response({'home_ads': serializer.data})
