# Generated by Django 4.2.5 on 2023-09-12 15:40

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmngugiwebsite', '0005_alter_blog_body'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CKEditorImage',
        ),
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=''),
        ),
    ]