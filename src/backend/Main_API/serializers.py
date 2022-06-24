from importlib_metadata import email
from rest_framework import serializers
from Main_API.models import Argument, Client, Job, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['id', 'username', 'password', 'email', 'client_id']


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job
        fields = ['id', 'name', 'description', 'input_type', 'input_amount', 'output_type', 'client_id']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields = ['id', 'business_name', 'ruc', 'payment_date', 'contact_email', 'contact_phone']


class ArgumentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Argument
        fields = ['id', 'job_id', 'arg_type', 'placeholder']


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField (
        max_length=255
    )

    password = serializers.CharField (
        max_length=255
    )

    client_id = serializers.IntegerField ()

    email = serializers.EmailField ()

    def create (self, validated_data):
        validated_data['client_id'] = Client.objects.get(id=validated_data['client_id'])
        return User.objects.create(**validated_data)


class ClientRegisterSerializer(serializers.Serializer):
    business_name = serializers.CharField (
        max_length=255,
    )

    ruc = serializers.IntegerField (
    )

    contact_email = serializers.EmailField ()

    contact_phone = serializers.IntegerField (
    )

    payment_date = serializers.DateField ()


class LoginDataSerializer(serializers.Serializer):
    username = serializers.CharField (
        max_length=255
    )
    
    password = serializers.CharField (
        max_length=255
    )