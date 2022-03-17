# Generated by Django 4.0.3 on 2022-03-16 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="timezone",
            field=models.CharField(
                choices=[
                    (-3, "UTC-3"),
                    (-2, "UTC-2"),
                    (-1, "UTC-1"),
                    (0, "UTC"),
                    (1, "UTC+1"),
                    (2, "UTC+2"),
                    (3, "UTC+3"),
                ],
                default=0,
                max_length=30,
            ),
            preserve_default=False,
        ),
    ]
