# Generated by Django 5.0.1 on 2024-01-19 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_remove_employee_salary_employee_interception'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='end_datetime',
        ),
    ]