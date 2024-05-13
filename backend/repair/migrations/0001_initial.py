# Generated by Django 5.0.1 on 2024-05-12 15:13

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repair_id', models.CharField(blank=True, max_length=8)),
                ('customer_name', models.CharField(max_length=30)),
                ('customer_phone_number', models.CharField(max_length=10)),
                ('phone_model', models.CharField(max_length=30)),
                ('repair_problem', models.CharField(max_length=50)),
                ('repair_description', models.TextField(blank=True, null=True)),
                ('imei_number', models.CharField(blank=True, max_length=30, null=True)),
                ('model_number', models.CharField(blank=True, max_length=30, null=True)),
                ('sim_tray', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], default='Present', max_length=20)),
                ('sim', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], default='Absent', max_length=20)),
                ('SD_card', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], default='Absent', max_length=20)),
                ('phone_cover', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], default='Absent', max_length=20)),
                ('phone_condition', models.CharField(blank=True, max_length=30, null=True)),
                ('total_amount', models.IntegerField()),
                ('advance_paid', models.IntegerField()),
                ('due', models.IntegerField()),
                ('received_date', models.DateField(default=datetime.datetime.now)),
                ('received_by', models.CharField(max_length=30)),
                ('repaired_by', models.CharField(blank=True, max_length=30, null=True)),
                ('delivery_date', models.DateField(default=datetime.datetime.now)),
                ('repair_status', models.CharField(choices=[('Not repaired', 'Not repaired'), ('Repaired', 'Repaired'), ('Unrepairable', 'Unrepairable'), ('Outrepaired', 'Outrepaired'), ('Completed', 'Completed')], default='Not repaired', max_length=20)),
                ('amount_paid', models.FloatField(blank=True, null=True)),
                ('repair_cost_price', models.FloatField(blank=True, null=True)),
                ('cost_price_description', models.CharField(blank=True, max_length=50, null=True)),
                ('repair_profit', models.FloatField(blank=True, null=True)),
                ('technician_profit', models.FloatField(blank=True, null=True)),
                ('my_profit', models.FloatField(blank=True, null=True)),
                ('outside_name', models.CharField(blank=True, max_length=30, null=True)),
                ('outside_desc', models.CharField(blank=True, max_length=30, null=True)),
                ('taken_by', models.CharField(blank=True, max_length=30, null=True)),
                ('outside_cost', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enterprise', to=settings.AUTH_USER_MODEL)),
                ('repairs', models.ManyToManyField(blank=True, related_name='enterprise_repairs', to='repair.repair')),
            ],
        ),
    ]