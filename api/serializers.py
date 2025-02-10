from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'id_type', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'id_type': {'read_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
