# Generated by Django 5.0.4 on 2024-05-06 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0004_historicalperformance_delete_performance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalperformance',
            name='average_response_time',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='historicalperformance',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='historicalperformance',
            name='fulfillment_rate',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='historicalperformance',
            name='on_time_delivery_rate',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='historicalperformance',
            name='quality_rating_avg',
            field=models.FloatField(blank=True),
        ),
    ]
