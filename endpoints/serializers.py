from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    done = serializers.BooleanField(read_only=True)

    class Meta:
        model = Todo
        fields = ["id", "title", "text", "deadline", "done"]
