# Generated by Django 5.0.4 on 2024-05-07 04:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0008_alter_historicalperformance_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalperformance',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.vendor', unique=True),
        ),
    ]
