from django.http import FileResponse
from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from JobExecuter.models import ExecutedJob, Status
from JobExecuter.serializers import ExecuteRequestSerializer, ExecutedJobSerializer, StatusSerializer
from JobExecuter.tasks import execute
from rest_framework.decorators import authentication_classes, permission_classes, api_view

# Create your views here.
class ExecutedJobViewSet(viewsets.ModelViewSet):
    queryset = ExecutedJob.objects.all()
    serializer_class = ExecutedJobSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ['id', 'job_id', 'user_id', 'status']
    search_fields = ['id', 'job_id', 'user_id', 'status']


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['id', 'job_status']


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def run_job(request, pk=None):
    serializer = ExecuteRequestSerializer (data=request.data)
    
    if serializer.is_valid():
        data = serializer.create(serializer.validated_data)
        return execute (request.data, data)
    else:
        error_body = {"error": serializer.errors}
        return Response(status=status.HTTP_400_BAD_REQUEST, data=error_body)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_output_file(request, pk=None):
    filename = request.query_params['file']
    return FileResponse(open(filename, 'rb'))
    