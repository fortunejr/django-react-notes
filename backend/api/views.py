from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Notes


class CreateUserView(generics.CreateAPIView):
    queryset=User.objects.all() #to make sure we dont create a user that already exists.
    serializer_class=UserSerializer #what kind of data we need to accept to create a new user
    permission_classes=[AllowAny] #to allow anyone to use this view ie create a new user

class NotesListCreate(generics.ListCreateAPIView):
    serializer_class=NoteSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return Notes.objects.filter(author=user) #you can only view notes that were written by you
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)
        return super().perform_create(serializer)


class NoteDelete(generics.DestroyAPIView):
    serializer_class=NoteSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return Notes.objects.filter(author=user)