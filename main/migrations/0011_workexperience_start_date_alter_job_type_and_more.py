# Generated by Django 4.0.3 on 2022-05-04 11:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_job_type_workexperience'),
    ]

    operations = [
        migrations.AddField(
            model_name='workexperience',
            name='start_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='type',
            field=models.CharField(choices=[('full_time', 'Full-time'), ('part_time', 'Part-time'), ('contract', 'Contract/Consultancy'), ('internship', 'Internship')], max_length=20),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='employment_type',
            field=models.CharField(choices=[('full_time', 'Full-time'), ('part_time', 'Part-time'), ('contract', 'Contract/Consultancy'), ('internship', 'Internship')], max_length=20),
        ),
    ]