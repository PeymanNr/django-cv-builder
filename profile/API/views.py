from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from io import BytesIO
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from profile.API.serializers import RegisterSerializer, ProfileSerializer, \
    SkillSerializer


class UserRegisterAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'username': user.username,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginAPIView(TokenObtainPairView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]


class ProfileDetailView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

class SkillsAPIView(CreateAPIView):
    serializer_class = SkillSerializer


class ProfilePDFView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        buffer = BytesIO()

        c = canvas.Canvas(buffer, pagesize=letter)
        c.setFont("Helvetica", 12)

        profile = request.user.profile
        c.drawString(100, 750, f"Name: {profile.user.username}")
        c.drawString(100, 735, f"Bio: {profile.bio}")
        c.drawString(100, 720, f"Job Experience: {profile.job_experience}")
        c.drawString(100, 705, f"Education: {profile.education}")
        c.drawString(100, 690, f"Certificates: {profile.certificates}")

        c.showPage()
        c.save()

        buffer.seek(0)

        response = HttpResponse(buffer, content_type="application/pdf")
        response['Content-Disposition'] = 'attachment; filename="profile.pdf"'

        return response