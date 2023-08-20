from rest_framework.authentication import TokenAuthentication
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from .serializers import CodeFileSerializer, CodeFile


class CodeFileViewSet(
    CreateModelMixin, ListModelMixin, DestroyModelMixin, GenericViewSet
):
    serializer_class = CodeFileSerializer
    authentication_classes = [TokenAuthentication, ]

    def get_queryset(self):
        return CodeFile.objects.filter(user=self.request.user)
