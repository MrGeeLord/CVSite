# Generated by Django 4.2.3 on 2023-09-13 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_blog_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='level',
            field=models.CharField(blank=True, choices=[('Beginner', 'Beginner'), ('Advanced', 'Advanced'), ('Expert', 'Expert'), ('Soft skill', 'Soft_skill')], max_length=20, null=True),
        ),
    ]
