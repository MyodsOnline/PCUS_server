# Generated by Django 4.1.1 on 2022-11-04 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zvk_getter', '0002_block_station_generator_block_station'),
    ]

    operations = [
        migrations.AddField(
            model_name='generator',
            name='main_condition',
            field=models.CharField(choices=[('KP', 'current_repair'), ('CP', 'mean_repair'), ('Bp', 'forced_downtime'), ('AP', 'emergency_repair'), ('KP', 'capital_repair'), ('P', 'in_work')], default='P', max_length=2, verbose_name='repair type'),
        ),
    ]