from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from files.serializers import CodeFileFrontSerializer, CodeFile
from reports.serializers import ReportFrontSerializer, Report
from reports.services import ReportReviewService
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from .forms import CustomUserCreationForm, UploadFileForm, CreateReportForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class CodeFileFrontViewSet(
    CreateModelMixin, ListModelMixin, GenericViewSet
):
    serializer_class = CodeFileFrontSerializer

    def get_queryset(self):
        return CodeFile.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = CodeFile(file=request.FILES['file'], user=request.user)
            instance.save()
            return HttpResponseRedirect(request.path_info)
        return HttpResponseRedirect(request.path_info)

    def list(self, request, *args, **kwargs):
        form = UploadFileForm()
        files_list = self.get_queryset()
        for file in files_list:
            file.file = str(file.file).split('/')[-1]

        return render(request, 'upload.html', {'files_list': files_list, 'form': form})


class FileDeleteView(DeleteView):
    model = CodeFile
    success_url = reverse_lazy('files_front-list')
    # template_name = 'delete_confirm.html'


class ReportFrontViewSet(
    CreateModelMixin, RetrieveModelMixin, ListModelMixin, GenericViewSet
):
    serializer_class = ReportFrontSerializer

    def get_queryset(self):
        return Report.objects.filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        form = CreateReportForm(user=request.user)
        return render(request, 'reports.html', {'reports_list': self.get_queryset(), 'form': form})

    def create(self, request, *args, **kwargs):
        try:
            instance = Report(
                file=CodeFile.objects.get(file=request.POST['files']),
                user=request.user
            )
            instance.save()
        except:
            return HttpResponseRedirect(request.path_info)
        return HttpResponseRedirect(request.path_info)

    def retrieve(self, request, *args, **kwargs):
        return render(request, 'report.html', {'report': self.get_object()})

    @action(detail=True, methods=['POST'], name='review')
    def review_report(self, request, pk=None):
        report = self.get_object()
        ReportReviewService(report).save_results()

        return HttpResponseRedirect(reverse_lazy('reports_front-list'))
