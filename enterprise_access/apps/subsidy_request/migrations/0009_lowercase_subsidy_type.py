# Generated by Django 3.2.12 on 2022-03-15 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subsidy_request', '0008_add_last_remind_date_on_subsidyconfig'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalsubsidyrequestcustomerconfiguration',
            name='subsidy_type',
            field=models.CharField(blank=True, choices=[('license', 'License Subsidy'), ('coupon', 'Coupon Subsidy')], help_text='Which type of subsidy is used to grant access.', max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='subsidyrequestcustomerconfiguration',
            name='subsidy_type',
            field=models.CharField(blank=True, choices=[('license', 'License Subsidy'), ('coupon', 'Coupon Subsidy')], help_text='Which type of subsidy is used to grant access.', max_length=32, null=True),
        ),
    ]
