# Generated by Django 4.2.3 on 2023-09-13 16:01

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_skill_image_icon_alter_skill_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
