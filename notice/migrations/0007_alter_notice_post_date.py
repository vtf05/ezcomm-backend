# Generated by Django 3.2.7 on 2021-11-21 09:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0006_alter_notice_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice_post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 21, 14, 48, 9, 712625)),
        ),
    ]
