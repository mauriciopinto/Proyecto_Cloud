from venv import create
from wsgiref import validate
from rest_framework import serializers
from JobExecuter.models import ExecutedJob, Status
from Main_API.models import Job, User

class ExecutedJobSerializer(serializers.ModelSerializer):
    class Meta:
        model=ExecutedJob
        fields = ['tagname', 'job_id', 'user_id', 'execution_time', 'status', 'running_time', 'output']


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Status
        fields = ['id', 'job_status']


class ExecuteRequestSerializer(serializers.Serializer):
    tagname = serializers.CharField()
    job_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    filename = serializers.CharField()
    data = serializers.CharField()
    arguments = serializers.ListField()

    def create(self, validated_data):
        validated_data['job_id'] = Job.objects.get(id=validated_data['job_id'])
        validated_data['user_id'] = User.objects.get(id=validated_data['user_id'])
        del validated_data['filename']
        del validated_data['data']
        del validated_data['arguments']
        return ExecutedJob.objects.create(**validated_data)
