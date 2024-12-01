from django.urls import path
from profile.API.views import UserRegisterAPIView, UserLoginAPIView, \
    ProfileDetailView, SkillsAPIView, ProfilePDFView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('profile/', ProfileDetailView.as_view(), name='profile'),
    path('profile/skills/', SkillsAPIView.as_view(), name='skills'),
    path('profile/pdf/', ProfilePDFView.as_view(), name='profile_pdf'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]