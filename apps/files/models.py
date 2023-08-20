import uuid
from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
from django.core.validators import FileExtensionValidator


def file_handler(instance, filename):
    return f'code_files/user_{instance.user.id}/{int(datetime.now().timestamp())}/{filename}'


class CodeFile(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    file = models.FileField(
        upload_to=file_handler,
        validators=[FileExtensionValidator(allowed_extensions=['py'])]
    )
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True, db_index=True)
