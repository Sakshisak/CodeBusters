# Generated by Django 2.2.2 on 2019-07-08 22:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_auto_20190708_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(default='', max_length=10, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
    ]
