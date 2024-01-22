from django.shortcuts import render
from .models import Event
from rest_framework import generics
from .serializers import EventSerializer

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

class EventListAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer