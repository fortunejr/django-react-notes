from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Notes

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id', 'username', 'password']
        #these are the field we will send and expect a return
        extra_kwargs={'password':{'write_only':True}}
        #this means we accept user when creating a new user but should not return password when giving info about the user ie fetch, it can only write not read
        
    def create(self, validated_data):
        user=User.objects.create_user(**validated_data)
        return user
        #this the the funtion thay will be called when we want to create a new version of this user



class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notes
        fields=['id','title','content','created_at','author']
        extra_kwargs = {'author': {'read_only': True}}