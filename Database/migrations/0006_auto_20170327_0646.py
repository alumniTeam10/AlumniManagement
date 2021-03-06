# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 06:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0005_auto_20170326_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='introduction',
            field=models.CharField(max_length=3000, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_dp',
            field=models.FileField(null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='active_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='branch_name',
            field=models.CharField(choices=[('Cse', 'Cse'), ('IT', 'IT'), ('Mechanical', 'Mechanical'), ('Civil', 'Civil'), ('Electrical', 'Electrical'), ('Electronics', 'Electronics')], default='Cse', max_length=50),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='course_name',
            field=models.CharField(choices=[('MTech', 'MTech'), ('BTech', 'BTech'), ('MS', 'MS')], default='BTech', max_length=40),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='create_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='current_organization_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='department_name',
            field=models.CharField(choices=[('Cse', 'Cse'), ('IT', 'IT'), ('Mechanical', 'Mechanical'), ('Civil', 'Civil'), ('Electrical', 'Electrical'), ('Electronics', 'Electronics')], default='Cse', max_length=50),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='designation',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='role',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='update_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='work_phone',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='active_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='create_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='department_name',
            field=models.CharField(choices=[('Cse', 'Cse'), ('IT', 'IT'), ('Mechanical', 'Mechanical'), ('Civil', 'Civil'), ('Electrical', 'Electrical'), ('Electronics', 'Electronics')], default='Cse', max_length=50),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='designation',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='update_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='active_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='branch_name',
            field=models.CharField(choices=[('Cse', 'Cse'), ('IT', 'IT'), ('Mechanical', 'Mechanical'), ('Civil', 'Civil'), ('Electrical', 'Electrical'), ('Electronics', 'Electronics')], default='Cse', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='course_name',
            field=models.CharField(choices=[('MTech', 'MTech'), ('BTech', 'BTech'), ('MS', 'MS')], default='BTech', max_length=40),
        ),
        migrations.AlterField(
            model_name='student',
            name='create_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='department_name',
            field=models.CharField(choices=[('Cse', 'Cse'), ('IT', 'IT'), ('Mechanical', 'Mechanical'), ('Civil', 'Civil'), ('Electrical', 'Electrical'), ('Electronics', 'Electronics')], default='Cse', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='update_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='create_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='update_date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type_flag',
            field=models.CharField(choices=[('admin', 'Admin'), ('student', 'Student'), ('alumni', 'Alumni'), ('faculty', 'Faculty')], default='alumni', max_length=10),
        ),
    ]
