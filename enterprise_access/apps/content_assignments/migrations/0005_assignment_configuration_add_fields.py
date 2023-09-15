# Generated by Django 3.2.20 on 2023-09-12 18:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('content_assignments', '0004_add_assignment_config_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignmentconfiguration',
            name='active',
            field=models.BooleanField(db_index=True, default=True, help_text='Whether this assignment configuration is active. Defaults to True.'),
        ),
        migrations.AddField(
            model_name='assignmentconfiguration',
            name='enterprise_customer_uuid',
            field=models.UUIDField(db_index=True, default=uuid.UUID('00000000-0000-0000-0000-000000000000'), help_text="The owning Enterprise Customer's UUID. Cannot be blank or null."),
        ),
        migrations.AddField(
            model_name='historicalassignmentconfiguration',
            name='active',
            field=models.BooleanField(db_index=True, default=True, help_text='Whether this assignment configuration is active. Defaults to True.'),
        ),
        migrations.AddField(
            model_name='historicalassignmentconfiguration',
            name='enterprise_customer_uuid',
            field=models.UUIDField(db_index=True, default=uuid.UUID('00000000-0000-0000-0000-000000000000'), help_text="The owning Enterprise Customer's UUID. Cannot be blank or null."),
        ),
    ]
