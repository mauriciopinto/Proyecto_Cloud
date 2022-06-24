from django import views
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action, authentication_classes, permission_classes, api_view

from Main_API.models import Argument, User, Job, Client
from Main_API.serializers import ArgumentSerializer, UserSerializer, JobSerializer, ClientSerializer, LoginDataSerializer, UserRegisterSerializer, ClientRegisterSerializer

import json

CREATED_RESOURCE_LOCATION_PREFIX = "http://localhost:8000/api/"

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ['id', 'client_id']
    search_fields = ['username', 'email']

    @action(detail=False, methods=['post'])
    def register (self, request, pk=None):
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid ():
            data = dict (serializer.validated_data)
            try:
                user = User.objects.get(username=data['username'])

                error_data = {
                    "error_message": "Este nombre de usuario ya está siendo utilizado."
                }

                return Response (status=status.HTTP_403_FORBIDDEN, data=error_data)

            except ObjectDoesNotExist:
                new_user = UserSerializer (serializer.save())

                headers = {
                    "Location": "{}users/{}".format(CREATED_RESOURCE_LOCATION_PREFIX, new_user.data['id']), 
                    "Content-Type": "application/json"
                }

                return Response (status=status.HTTP_201_CREATED, data=new_user.data, headers=headers)


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ['id', 'client_id']
    search_fields = ['name']

    """def list(self, request, *args, **kwargs):
        
        headers = {
                "Content-Type": "application/json",
                "Access-Control-Allow-Credentials": "true"
            }

        job_list = []
        jobs = None
        if 'client_id' in request.query_params:
            jobs = self.queryset.filter(client_id=request.query_params['client_id'])
        
        else:
            jobs = self.queryset

        for job in jobs:
            serialized_job = JobSerializer (job)
            job_list.append (serialized_job.data)
        
        return Response (status=status.HTTP_200_OK, data=job_list, headers=headers)"""
    


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['id', 'ruc']
    search_fields = ['business_name']

    @action(detail=False, methods=['post'])
    def register (self, request, pk=None):
        serializer = ClientRegisterSerializer (request.data)

        if serializer.is_valid ():
            data = dict(serializer.validated_data)
            try:
                client = Client.objects.get(ruc=data['ruc'])

                error_data = {
                    "error_message": "El RUC especificado ya se encuentra registrado"
                }

                return Response(status=status.HTTP_403_FORBIDDEN, data=error_data)

            except ObjectDoesNotExist:
                new_client = ClientSerializer (serializer.save())

                headers = {
                    "Location": "{}/clients/{}".format(CREATED_RESOURCE_LOCATION_PREFIX, new_client.data["id"]),
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                }

                return Response(status=status.HTTP_201_CREATED, data=new_client.data, headers=headers)


class ArgumentViewSet(viewsets.ModelViewSet):
    queryset = Argument.objects.all()
    serializer_class = ArgumentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ['id', 'job_id']
    search_fields = ['arg_type', 'placeholder']


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def user_login (request):
    serializer = LoginDataSerializer (data=request.data)

    headers = {
                "Content-Type": "application/json",
                "Access-Control-Allow-Credentials": "true"
            }

    if serializer.is_valid():
        data = dict(serializer.validated_data)
        try:
            user = User.objects.get (username=data["username"])
            user_data = UserSerializer (user).data 

            if data['password'] != user_data['password']:
                print ("wrong password")
                raise ObjectDoesNotExist

            
            request.session['logged'] = True
            request.session['user_id'] = user_data['id']

            return Response(status=status.HTTP_200_OK, data=user_data, headers=headers)

        except ObjectDoesNotExist:
            
            error_data = {
                "error_message": "Usuario o contraseña incorrectos"
            }

            return Response(status=status.HTTP_404_NOT_FOUND, data=error_data, headers=headers)

    else:
        error_data = {
                "error_message": "Datos invalidos o incompletos"
            }

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data=error_data)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_session_user (request):

    headers = {
                "Content-Type": "application/json",
                "Access-Control-Allow-Credentials": "true"
            }

    if 'logged' in request.session and 'user_id' in request.session:
        user = User.objects.get (id=request.session['user_id'])
        user_data = UserSerializer (user).data
        return Response (status=status.HTTP_200_OK, data=user_data, headers=headers)
    
    else:
        error_data = {
            "error_message": "No has iniciado sesión correctamente"
        }

        return Response(status=status.HTTP_404_NOT_FOUND, data=error_data, headers=headers)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def close_session (request):
    headers = {
                "Content-Type": "application/json",
                "Access-Control-Allow-Credentials": "true"
            }

    if 'logged' in request.session and 'user_id' in request.session:
        del request.session['logged']
        del request.session['user_id']
        return Response (status=status.HTTP_200_OK, headers=headers)
    
    else:
        error_data = {
            "error_message": "No has iniciado sesión correctamente"
        }

        return Response(status=status.HTTP_404_NOT_FOUND, data=error_data, headers=headers)