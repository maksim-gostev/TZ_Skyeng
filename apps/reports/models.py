from django.db import models
from django.contrib.auth import get_user_model


class Status(models.Choices):
    pending = 'pending'
    reviewed = 'reviewed'


class Report(models.Model):
    file = models.OneToOneField(
        'files.CodeFile',
        on_delete=models.CASCADE,
        primary_key=True
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    result = models.JSONField(null=True, blank=True)

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.pending)

    created = models.DateTimeField(auto_now_add=True, db_index=True)
    is_sent = models.BooleanField(default=False, db_index=True)
