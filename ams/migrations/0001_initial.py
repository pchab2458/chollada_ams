# Generated by Django 4.1.3 on 2022-11-21 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_ref', models.CharField(max_length=6)),
                ('bill_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('open', 'OPEN'), ('close', 'CLOSE')], default='open', max_length=5)),
                ('tenant_name', models.CharField(max_length=100)),
                ('room_no', models.CharField(max_length=4)),
                ('room_cost', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('room_acc_cost', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('electricity_cost', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('water_cost', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('common_ser_cost', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('other_ser_cost', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('overdue_amount', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('adjust', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('bill_total', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('payment_amount', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('cf_amount', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('late_fee', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('maint_cost', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
            ],
            options={
                'ordering': ('-bill_date',),
            },
        ),
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=100)),
                ('cpu', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Room_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=250)),
                ('rate', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='TenantProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.CharField(max_length=13, unique=True)),
                ('phone', models.CharField(max_length=10)),
                ('term', models.PositiveSmallIntegerField(default=12)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('deposit', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('deduct', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('cum_ovd', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7)),
                ('adjust', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('photo', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/')),
                ('bill_date', models.DateField(auto_now=True)),
                ('elec_unit', models.DecimalField(decimal_places=2, max_digits=7, null=True)),
                ('water_unit', models.DecimalField(decimal_places=2, max_digits=7, null=True)),
                ('late_fee', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('maint_cost', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('extra', models.ManyToManyField(to='ams.extra')),
                ('room_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ams.room')),
                ('tenant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ams.room_type'),
        ),
        migrations.CreateModel(
            name='MaintenanceCharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=100)),
                ('job_cost', models.DecimalField(decimal_places=2, max_digits=7)),
                ('status', models.CharField(choices=[('open', 'OPEN'), ('close', 'CLOSE')], default='open', max_length=5)),
                ('job_date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('room_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ams.room')),
            ],
            options={
                'ordering': ('-job_date',),
            },
        ),
    ]