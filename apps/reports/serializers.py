from rest_framework import serializers
from .models import Report


class ReportFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['file', 'user', 'result', 'status', 'created', 'is_sent']
