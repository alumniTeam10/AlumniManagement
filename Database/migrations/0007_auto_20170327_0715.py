# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0006_auto_20170327_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni',
            name='current_organization_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='designation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='role',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='work_phone',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='designation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='introduction',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_dp',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='user',
            name='secret_question',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='secret_question_answer',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]