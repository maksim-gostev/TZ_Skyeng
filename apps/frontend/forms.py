from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import FileExtensionValidator

from files.models import CodeFile


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2')


class UploadFileForm(forms.Form):
    file = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['py'])])


class CreateReportForm(forms.Form):
    files = forms.ModelChoiceField(queryset=CodeFile.objects.none())

    def __init__(self, user):
        super(CreateReportForm, self).__init__()
        self.fields['files'].queryset = CodeFile.objects.filter(user=user).values_list('file', flat=True)
