from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import SignUpView, CodeFileFrontViewSet, ReportFrontViewSet, FileDeleteView

router = SimpleRouter()
router.register('files', CodeFileFrontViewSet, basename='files_front')
router.register('reports', ReportFrontViewSet, basename='reports_front')

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("", include("django.contrib.auth.urls")),
    path('', include(router.urls)),
    path('delete/<uuid:pk>', FileDeleteView.as_view(), name='delete_file')
]
