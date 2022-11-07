from rest_framework import serializers

from .forms import CreateUserForm
from .models import *

class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CreateUserForm
        fields = ('username', 'email', 'password1', 'password2')

        extra_kwargs = {
                'password1':{'write_only':True},
                'password2':{'write_only':True},
        }   
    def save(self):
        account = User(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
        )
        password1 = self.validated_data['password1']
        password2 = self.validated_data['password2']

        if password1 != password2:
            raise serializers.ValidationError({'password: Passwords must match'})
        account.set_password(password1)
        account.save()
        return account



class BeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beat
        fields = ('title', 'duration', 'audio', 'untagged_audio', 'cover', 
        'genre', 'tempo', 'key', 'price', 'date_added')

        def create(self, validated_data):
            beat = Beat.objects.create(validated_data['title'], validated_data['duration'], 
            validated_data['untagged_audio'], validated_data['cover'], 
            validated_data['genre'], validated_data['tempo'], validated_data['key'], 
            validated_data['price'], validated_data['date_added'])

            return beat

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'message')

    def create(self, validated_data):
        return super().create(validated_data['name']. validated_date['email'], validated_data['message'])