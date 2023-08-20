from rest_framework import serializers
from .models import CodeFile


class CodeFileFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeFile
        fields = ['file', 'user', 'created', 'updated']
