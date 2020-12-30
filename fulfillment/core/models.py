from django.db import models


class TimeStampedModel(models.Model):

    created_dt = models.DateTimeField(auto_now_add=True)
    modified_dt = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
