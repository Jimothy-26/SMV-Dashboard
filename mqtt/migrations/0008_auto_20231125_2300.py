# Generated by Django 3.2.13 on 2023-11-26 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mqtt', '0007_auto_20231125_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagehistory',
            name='trip',
            field=models.ForeignKey(blank=None, default=None, on_delete=django.db.models.deletion.CASCADE, to='mqtt.trip'),
        ),
        migrations.AlterField(
            model_name='mqtterror',
            name='trip',
            field=models.ForeignKey(blank=None, default=None, on_delete=django.db.models.deletion.CASCADE, to='mqtt.trip'),
        ),
    ]