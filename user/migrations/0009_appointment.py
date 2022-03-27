# Generated by Django 4.0.2 on 2022-03-26 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_blog_draft'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=500)),
                ('appointment_date', models.DateField(max_length=500)),
                ('appointment_start_time', models.DateTimeField(max_length=500)),
                ('appointment_end_time', models.DateTimeField(max_length=500)),
            ],
        ),
    ]
