from rest_framework import generics,status
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import User
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

class UserView(APIView):

    serializer_class = UserSerializer

    def post(self,request):
        serializer_obj = self.serializer_class(data=request.data)
        serializer_obj.is_valid(raise_exception=True)
        serializer_obj.save()
        user_data = serializer_obj.data
         
        return Response(user_data,status=status.HTTP_201_CREATED)
    def get(self,request):
        queryset = User.objects.all()
        serializer_obj = self.serializer_class(queryset,many = True)
        
        return Response(serializer_obj.data,status=status.HTTP_200_OK)

class UserUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
        
    
def home(request):
    return render(request,"home.html")
def sign_up(request):
    return render(request,"signUp.html")
def login(request):
    return render(request,"login.html")