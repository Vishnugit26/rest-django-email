from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserSerializer

@api_view(['POST'])
def register(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        # Send email after successful registration
        send_mail(
            'Welcome to ekandhathayude aparatheeram',
            'Thank you for visiting at sogha ganam. enjoy the sadness ;( . Click the link below to login: https://youtu.be/fCbmw-DPHvs?si=tnfz87VHmKwI0Txy' + user.email,
            'vishnudinesh111@gmail.com',
            [user.email],
            fail_silently=False,
        )
        return Response({'message': 'User registered successfully and email sent.'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

