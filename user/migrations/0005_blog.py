# Generated by Django 4.0.2 on 2022-03-21 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_profile_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('category', models.CharField(choices=[('Mental Health', 'Mental Health'), ('Heart Disease', 'Heart Disease'), ('Covid19', 'Covid19'), ('Immunization', 'Immunization')], default='none', max_length=100)),
                ('summary', models.TextField()),
                ('content', models.TextField()),
            ],
        ),
    ]
