# Generated by Django 4.2.3 on 2023-09-11 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_skill_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='score',
        ),
        migrations.AlterField(
            model_name='certificate',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
