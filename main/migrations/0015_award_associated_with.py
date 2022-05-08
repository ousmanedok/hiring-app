# Generated by Django 4.0.3 on 2022-05-06 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_merge_20220506_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='associated_with',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='experience_awards', to='main.workexperience'),
            preserve_default=False,
        ),
    ]
