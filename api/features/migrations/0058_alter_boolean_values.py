# Generated by Django 3.2.19 on 2023-06-14 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0057_add_feature_is_server_key_only'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featurestatevalue',
            name='boolean_value',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalfeaturestatevalue',
            name='boolean_value',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]