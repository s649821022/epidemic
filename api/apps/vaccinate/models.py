from core.models import TimeStampedModel
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Vaccinate(TimeStampedModel):
    name = models.CharField(_("接种人姓名"), max_length=20)
    card = models.CharField(_("身份证号"), max_length=18)
    phone = models.CharField(_("联系电话"), max_length=11)
    address = models.CharField(_("联系地址"), max_length=64)
    vaccinateNo = models.CharField(_("接种次数"), max_length=4)
    vaccinateTime = models.CharField(_("接种时间"), max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="记录员", related_name="vaccinate")

    class Meta:
        db_table = "vaccinate"
