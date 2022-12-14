# Generated by Django 4.0.4 on 2022-06-06 03:33

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccinate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created_at')),
                ('modified_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified_at')),
                ('name', models.CharField(max_length=20, verbose_name='接种人姓名')),
                ('card', models.CharField(max_length=18, verbose_name='身份证号')),
                ('phone', models.CharField(max_length=11, verbose_name='联系电话')),
                ('address', models.CharField(max_length=64, verbose_name='联系地址')),
                ('vaccinateNo', models.CharField(max_length=4, verbose_name='接种次数')),
                ('vaccinateTime', models.CharField(max_length=10, verbose_name='接种时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vaccinate', to=settings.AUTH_USER_MODEL, verbose_name='记录员')),
            ],
            options={
                'db_table': 'vaccinate',
            },
        ),
    ]
