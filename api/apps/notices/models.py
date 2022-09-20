from core.models import TimeStampedModel
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Notices(TimeStampedModel):
    title = models.CharField(_("通知标题"), max_length=32)
    detail = models.CharField(_("检查详情"), max_length=125)

    class Meta:
        db_table = "notices"
