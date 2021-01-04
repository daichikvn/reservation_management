from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime


class Schedule(models.Model):
    class Meta:
        db_table = "schedule"
        verbose_name ="スケジュール"
        verbose_name_plural ="スケジュール"

    date = models.DateField(verbose_name="日付", default=datetime.now)
    time = models.CharField(verbose_name="時間", help_text="(例: 18:00)", max_length=10)
    name = models.CharField(verbose_name="予約者名", max_length=255)
    num_of_people = models.IntegerField(verbose_name="人数", help_text="(例: 2)")
    tel_number = models.CharField(verbose_name='電話番号', max_length=15, blank=True, help_text="任意")
    memo = models.TextField(verbose_name="備考", max_length=500, blank=True, help_text="任意")
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    def __str__(self):
        return '{0} {1} {2}'.format(self.date, self.time, self.name)