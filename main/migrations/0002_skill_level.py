# Generated by Django 3.2.20 on 2023-07-27 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='level',
            field=models.CharField(blank=True, choices=[('Beginner', 'Beginner'), ('Advanced', 'Advanced'), ('Expert', 'Expert')], max_length=20, null=True),
        ),
    ]
