# Generated by Django 4.2 on 2024-01-26 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboard_user',
            name='enrolled_batches',
        ),
    ]
