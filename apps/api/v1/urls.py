from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .files import CodeFileViewSet
from .reports import ReportViewSet

router = SimpleRouter()


router.register('files', CodeFileViewSet, basename='files')
router.register('reports', ReportViewSet, basename='reports')


urlpatterns = [
    path('', include(router.urls)),
]
