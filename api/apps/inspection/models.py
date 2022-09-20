from core.models import TimeStampedModel
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Inspection(TimeStampedModel):
    location = models.CharField(_("检查地点"), max_length=64)
    result = models.CharField(_("检查结果"), max_length=2)
    detail = models.CharField(_("检查详情"), max_length=125)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="记录员", related_name="inspection")

    class Meta:
        db_table = "inspection"
