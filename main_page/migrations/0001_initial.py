# Generated by Django 2.2rc1 on 2019-03-26 14:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='dog_image')),
                ('breed', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('contact', models.IntegerField()),
                ('address', models.TextField()),
                ('additional_info', models.TextField()),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2019, 3, 26, 14, 49, 14, 930179, tzinfo=utc))),
            ],
        ),
    ]
