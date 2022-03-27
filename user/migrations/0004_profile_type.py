# Generated by Django 4.0.2 on 2022-03-16 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_profile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='type',
            field=models.CharField(choices=[('Patient', 'Patient'), ('Doctor', 'Doctor')], default='none', max_length=100),
        ),
    ]
