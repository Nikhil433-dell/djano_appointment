# Generated by Django 4.0.2 on 2022-03-21 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_blog_draft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='draft',
            field=models.BooleanField(default=False),
        ),
    ]