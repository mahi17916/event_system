from rest_framework import generics
from .models import events,Registration
from .serializers import eventSerializer, RegistrationSerializer

class eventListView(generics.ListCreateAPIView):
    queryset = events.objects.all()
    serializer_class = eventSerializer
    
class eventDetailView(generics.RetrieveAPIView):
    queryset = events.objects.all()
    serializer_class = eventSerializer
    
class RegistrationCreateView(generics.CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

class RegistrationListView(generics.ListAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    


