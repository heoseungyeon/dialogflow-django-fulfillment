from django.db import models
from accounts.models import User
from core.models import TimeStampedModel
# Create your models here.


class Memo(TimeStampedModel):
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'memobot_memo'
        verbose_name = 'memo'
        verbose_name_plural = 'memos'