import os

from api.apps.core.validators import FileValidator
from django.contrib.auth.models import AbstractUser
from django.core.files.base import ContentFile
from django.db import models
from django.utils.translation import gettext_lazy as _
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from users.avatar_generator import AvatarGenerator


def user_avatar_path(instance, filename):
    return os.path.join("users", "avatars", instance.username, filename)


class User(AbstractUser):
    AVATAR_MAX_SIZE = 2 * 1024 * 1024
    AVATAR_ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg"]
    AVATAR_DEFAULT_FILENAME = "default.jpeg"
    LEVEL_TYPE = ((0, "普通用户"), (1, "管理员"))
    level = models.CharField(max_length=50, verbose_name="角色", choices=LEVEL_TYPE, default=0, null=False)
    avatar = models.ImageField(
        _("avatar"),
        upload_to=user_avatar_path,
        validators=[FileValidator(max_size=AVATAR_MAX_SIZE, allowed_extensions=AVATAR_ALLOWED_EXTENSIONS)],
        blank=True,
    )
    avatar_thumbnail = ImageSpecField(
        source="avatar",
        processors=[ResizeToFill(70, 70)],
        format="jpeg",
        options={"quality": 100},
    )

    class Meta:
        db_table = "user"
        verbose_name = "用户表"
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        if not self.pk:
            if not self.avatar:
                self.set_default_avatar()
        super(User, self).save(*args, **kwargs)

    def set_default_avatar(self):
        avatar_byte_array = AvatarGenerator.generate(self.username)
        self.avatar.save(
            self.AVATAR_DEFAULT_FILENAME,
            ContentFile(avatar_byte_array),
            save=False,
        )
