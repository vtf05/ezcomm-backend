# Generated by Django 3.2.7 on 2021-11-17 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice_post',
            name='is_assignment',
            field=models.BooleanField(default=False),
        ),
    ]
