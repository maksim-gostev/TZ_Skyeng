from rest_framework import serializers
from files.models import CodeFile


class CodeFileSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CodeFile
        fields = ['uid', 'file', 'user', 'created', 'updated']
