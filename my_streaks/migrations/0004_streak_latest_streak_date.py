# Generated by Django 4.2.5 on 2023-11-08 21:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_streaks', '0003_streak_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='streak',
            name='latest_streak_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
