# Generated by Django 5.0.4 on 2024-05-10 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_alter_studentprofile_earned_points_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10, null=True),
        ),
    ]
