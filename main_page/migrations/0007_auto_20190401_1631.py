# Generated by Django 2.1.1 on 2019-04-01 11:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0006_auto_20190401_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contact',
            field=models.IntegerField(default='00'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 1, 11, 1, 34, 758613, tzinfo=utc)),
        ),
    ]