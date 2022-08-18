from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CustomUserSerializer
from .models import CustomUser


class CustomUserView(APIView):
    """Users API View"""

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response({'users': serializer.data})

    def post(self, request, *args, **kwargs):
        user_data = request.data

        serializer = CustomUserSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save()

        return Response({'success': f'User {user_data["username"]} created'})


class CustomUserDetailView(APIView):
    """CustomUser Details API View"""

    def get(self, request, pk):
        user = CustomUser.objects.get(id=pk)
        serializer = CustomUserSerializer(user)
        return Response({'user': serializer.data})

    def delete(self, request, pk):
        user = CustomUser.objects.get(id=pk)
        user.delete()

        return Response({'success': f'Advertisement deleted successfully!'})
