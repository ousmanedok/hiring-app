# Generated by Django 3.2.9 on 2022-05-05 08:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0009_teammember_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_university', models.CharField(max_length=100)),
                ('field_of_study', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('grade', models.CharField(max_length=100)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('is_current', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField()),
                ('school_website_url', models.URLField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_educations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]