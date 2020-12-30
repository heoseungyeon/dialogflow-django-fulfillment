from django.db import models
from accounts.models import User
from memo.models import Memo
from core.models import TimeStampedModel
# Create your models here.


class Alarm(TimeStampedModel):
    alarmTime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    memo = models.ForeignKey(Memo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'memobot_alarm'
        verbose_name = 'alarm'
        verbose_name_plural = 'alarms'
