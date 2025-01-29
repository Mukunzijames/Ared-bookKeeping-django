from rest_framework import serializers
from .models import ToDo, User

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id', 'created', 'title', 'description', 'completed', 'due_date']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'created_at', 'updated_at']
        extra_kwargs = {'password': {'write_only': True}} 