from django.urls import path
from . import views
from .api_view import CustomUserView, CustomUserDetailView


urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('activate/<uid64>/<token>', views.VerificationView.as_view(), name='activate'),
    path('private/', views.private, name='private'),
    # api urls
    path('users/', CustomUserView.as_view()),
    path('users/<int:pk>/', CustomUserDetailView.as_view()),
]

