# Generated by Django 3.0.6 on 2020-05-23 08:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200523_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 23, 8, 19, 10, 276753, tzinfo=utc)),
        ),
    ]
