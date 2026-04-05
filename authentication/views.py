from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from authentication.models import User

# Create your views here.
class SignUpView(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request):
        
        email = request.data['email']
        username = request.data['username']
        password = request.data['password']
        if not email:
            return Response({'error': True, 'error_msg': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
        if not username:
            return Response({'error': True, 'error_msg': 'Username is required'}, status=status.HTTP_400_BAD_REQUEST)
        if not password:
            return Response({'error': True, 'error_msg': 'Password is required'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({'error': True, 'error_msg': 'Email already in use'})
        if User.objects.filter(username=username).exists():
            return Response({'error': True, 'error_msg': 'Username already in use'})
        User.objects.create_user(email=email, username=username, password=password)
        return Response({"message": "Please login back with same credentials"})