from reports.services import ReportReviewService
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action, authentication_classes, api_view
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.viewsets import GenericViewSet

from .serializers import ReportSerializer, Report, ReportCreateSerializer


class ReportViewSet(
    CreateModelMixin, RetrieveModelMixin, ListModelMixin, GenericViewSet
):
    serializer_class = ReportSerializer
    authentication_classes = [TokenAuthentication, ]

    def get_queryset(self):
        return Report.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReportSerializer
        elif self.request.method == 'POST':
            return ReportCreateSerializer

    @action(detail=True, methods=['POST'], name='review')
    def review_report(self, request, pk=None):
        report = self.get_object()
        ReportReviewService(report).save_results()

        return Response(status=HTTP_201_CREATED)
