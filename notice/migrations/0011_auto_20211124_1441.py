# Generated by Django 3.2.7 on 2021-11-24 09:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0010_auto_20211124_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment_post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 24, 9, 11, 44, 596321, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='notice_post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 24, 9, 11, 44, 595322, tzinfo=utc)),
        ),
    ]
