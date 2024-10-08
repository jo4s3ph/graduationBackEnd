# Generated by Django 5.0.4 on 2024-04-27 09:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_admin', '0002_area_is_active_event_is_active_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='faculty_name',
        ),
        migrations.CreateModel(
            name='FacultyDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(blank=True, max_length=100)),
                ('faculty_name', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_ubdated', models.DateField(auto_now=True, null=True)),
                ('admin_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system_admin.systemadminprofile')),
            ],
            options={
                'db_table': 'faculty_department',
            },
        ),
        migrations.AddField(
            model_name='area',
            name='faculty_department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system_admin.facultydepartment'),
        ),
        migrations.AddField(
            model_name='event',
            name='faculty_department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system_admin.facultydepartment'),
        ),
    ]
