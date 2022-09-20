from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.fields import AutoCreatedField, AutoLastModifiedField


class TimeStampedModel(models.Model):
    created_at = AutoCreatedField(_("created_at"))  # 创建时间
    modified_at = AutoLastModifiedField(_("modified_at"))  # 修改时间

    class Meta:
        abstract = True  # 抽象类，不在数据库中创建此表
