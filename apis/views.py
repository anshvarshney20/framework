from django.shortcuts import render
from rest_framework import generics
from apis.models import Register
from apis.serializers import RegisterSerializers

def home(request):
    return render(request,'plates/index.html')


class getData(generics.ListCreateAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializers

class putData(generics.RetrieveUpdateDestroyAPIView):
    queryset = Register
    serializer_class = RegisterSerializers
