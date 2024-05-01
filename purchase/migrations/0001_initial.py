# Generated by Django 5.0.4 on 2024-05-01 07:54

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_number', models.CharField(max_length=100, verbose_name='Unique Product Order No')),
                ('order_date', models.DateTimeField(auto_now_add=True, verbose_name='Order Date')),
                ('delivery_date', models.DateTimeField(auto_now=True, verbose_name='Expected Delivery Date')),
                ('items', models.JSONField()),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], max_length=100)),
                ('quality_rating', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('issue_date', models.DateTimeField(auto_now=True)),
                ('acknowledgement_date', models.DateField(auto_now_add=True, null=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.vendor')),
            ],
        ),
    ]
