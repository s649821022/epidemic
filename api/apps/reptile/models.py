from core.models import TimeStampedModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class Reptile(TimeStampedModel):
    """
    疫情数据统计，数据从网上爬取
    由于数据都是正整数，所以使用PositiveIntegerField
    """

    currentConfirmedCount = models.PositiveIntegerField(_("现存确诊人数"), default=0)
    confirmedCount = models.PositiveIntegerField(_("累计确诊人数"), default=0)
    suspectedCount = models.PositiveIntegerField(_("累计境外确诊人数"), default=0)
    curedCount = models.PositiveIntegerField(_("累计治愈人数"), default=0)
    deadCount = models.PositiveIntegerField(_("累计死亡人数"), default=0)
    seriousCount = models.PositiveIntegerField(_("当前无症状人数"), default=0)
    suspectedIncr = models.PositiveIntegerField(_("新增境外输入人数"), default=0)
    currentConfirmedIncr = models.PositiveIntegerField(_("相比昨天现存确诊人数"), default=0)
    confirmedIncr = models.PositiveIntegerField(_("	相比昨天累计确诊人数"), default=0)
    curedIncr = models.PositiveIntegerField(_("相比昨天新增治愈人数"), default=0)
    deadIncr = models.PositiveIntegerField(_("相比昨天新增死亡人数"), default=0)
    seriousIncr = models.IntegerField(_("相比昨天现存无症状人数"), default=0)
    yesterdayConfirmedCountIncr = models.PositiveIntegerField(_("相比昨天新增累计确诊人数"), default=0)
    yesterdaySuspectedCountIncr = models.PositiveIntegerField(_("相比昨天境外输入确诊人数"), default=0)
    highDangerCount = models.PositiveIntegerField(_("国内高风险地区个数"), default=0)
    midDangerCount = models.PositiveIntegerField(_("国内中风险地区个数"), default=0)

    class Meta:
        db_table = "reptile"
