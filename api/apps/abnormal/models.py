from core.models import TimeStampedModel
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Abnormal(TimeStampedModel):
    detail = models.CharField(_("检查详情"), max_length=125)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="记录员", related_name="abnormal")

    class Meta:
        db_table = "abnormal"
