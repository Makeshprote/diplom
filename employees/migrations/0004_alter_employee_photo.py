# Generated by Django 5.0.1 on 2024-01-23 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_remove_event_end_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photo/'),
        ),
    ]
